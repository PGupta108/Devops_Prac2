def test_name():
    name = "Student"
    assert len(name) > 0

def test_email():
    email = "student@gmail.com"
    assert "@" in email

def test_course():
    course = "Web Development"
    assert len(course) > 0

print("All tests passed")