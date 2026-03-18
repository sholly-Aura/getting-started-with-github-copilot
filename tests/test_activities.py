def test_get_activities_returns_all(client):
    # Arrange
    # (state is provided by the app fixture)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "Programming Class" in data

    chess = data["Chess Club"]
    assert isinstance(chess, dict)
    assert "participants" in chess
    assert "michael@mergington.edu" in chess["participants"]
