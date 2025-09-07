def transform_dataset(data):
    # Your solution here
    qualified_students = {}
    subject_summary = {}
    
    # Step 1: Calculate average grade for each student and filter qualified students
    # (students with all grades above 70)
    for record in data:
        grades = record.get('grades', [])
        if not grades:
            continue

        if all(grade > 70 for grade in grades):
            avg = round(sum(grades) / len(grades), 2)
            stdid = record.get('student_id')
            qualified_students[stdid] = avg
    
    # Step 2: Create a summary of subjects taken by qualified students
            for subject in record.get('subjects', []):
                subject_summary[subject] = subject_summary.get(subject, 0) + 1
    
    # Step 3: Return the final dictionary with qualified_students and subject_summary
    return {
        "qualified_students": qualified_students,
        "subject_summary": subject_summary
    }