from flask import Flask, jsonify, request, Response
from src.web.talks_repository import TalksRepository
from src.talk import Talk

app = Flask('track_management')
app.talks_repository = TalksRepository()


@app.route('/talks', methods=['POST'])
def talks():
    title = request.form['title']
    duration = request.form.get('duration', type=int)
    app.talk = Talk(title, duration)
    talk_id = app.talks_repository.insert(app.talk)
    talk = app.talks_repository.get(talk_id)

    return jsonify({'id': talk_id, 'title': talk.title, 'duration':
                    talk.duration})


@app.route('/talks/<int:talk_id>', methods=['DELETE'])
def delete_talk(talk_id):
    app.talks_repository.delete(talk_id)

    return Response(status=204)
