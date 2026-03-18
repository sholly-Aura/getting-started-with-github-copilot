from urllib.parse import quote


def test_signup_student_success(client):
    # Arrange
    activity = "Chess Club"
    email = "test_student@mergington.edu"
    url = f"/activities/{quote(activity)}/signup?email={email}"

    # Act
    response = client.post(url)

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity}"

    # Verify the student is now in the participants list
    activities = client.get("/activities").json()
    assert email in activities[activity]["participants"]


def test_signup_nonexistent_activity_returns_404(client):
    # Arrange
    activity = "Nonexistent Club"
    email = "student@mergington.edu"
    url = f"/activities/{quote(activity)}/signup?email={email}"

    # Act
    response = client.post(url)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_duplicate_returns_400(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # already signed up
    url = f"/activities/{quote(activity)}/signup?email={email}"

    # Act
    response = client.post(url)

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up"


def test_unregister_student_success(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"
    url = f"/activities/{quote(activity)}/signup?email={email}"

    # Act
    response = client.delete(url)

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {email} from {activity}"

    activities = client.get("/activities").json()
    assert email not in activities[activity]["participants"]


def test_unregister_not_signed_up_returns_404(client):
    # Arrange
    activity = "Chess Club"
    email = "not_signed_up@mergington.edu"
    url = f"/activities/{quote(activity)}/signup?email={email}"

    # Act
    response = client.delete(url)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student not signed up"


def test_unregister_nonexistent_activity_returns_404(client):
    # Arrange
    activity = "Nonexistent Club"
    email = "student@mergington.edu"
    url = f"/activities/{quote(activity)}/signup?email={email}"

    # Act
    response = client.delete(url)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
