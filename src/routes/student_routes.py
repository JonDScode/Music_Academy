from flask import Blueprint, request, jsonify
from src.services import student_service
from src.db.database import db

student_bp = Blueprint('student', __name__)

@student_bp.route('/students/', methods=['POST'])
def create_student():
    data = request.json
    new_student = student_service.create_student(db.session, data)
    return jsonify(new_student.to_dict()), 201

@student_bp.route('/students/<int:student_id>', methods=['GET'])
def read_student(student_id):
    student = student_service.get_student(db.session, student_id)
    if student is None:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student.to_dict())

@student_bp.route('/students', methods=['GET'])
def list_students():
    students = student_service.get_all_students(db.session)
    return jsonify([student.to_dict() for student in students])

@student_bp.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.json
    updated_student = student_service.update_student(db.session, student_id, data)
    if updated_student is None:
        return jsonify({"error": "Student not found or update failed"}), 404
    return jsonify(updated_student.to_dict())

@student_bp.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    deleted_student = student_service.delete_student(db.session, student_id)
    if deleted_student is None:
        return jsonify({"error": "Student not found or delete failed"}), 404
    return '', 204


# Añade más rutas para actualizar, eliminar, etc.
