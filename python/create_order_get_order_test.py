# Татьяна Трешникова, 11-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_get_order_by_track_get_success_response():
    create_order_response = sender_stand_request.post_new_order()
    track = create_order_response.json()["track"]
    get_order_response = sender_stand_request.get_order_by_track(track)

    assert get_order_response.status_code == 200

