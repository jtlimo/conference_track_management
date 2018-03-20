import json
from flask import Flask, jsonify, request, Response, render_template
from src.web.talks_repository import TalksRepository, TalkNotFoundException
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

@app.route('/talks', methods=['GET'])
def list_talks():
    talks_json = []
    talks = app.talks_repository.get()
    for talk in talks:
      talks_json.append({'title': talk.title, 'duration': talk.duration})
    return json.dumps(talks_json)

@app.route('/talks/<int:talk_id>', methods=['DELETE'])
def delete_talk(talk_id):
  try:
      app.talks_repository.delete(talk_id)
  except TalkNotFoundException:
      return not_found(404)

  return Response(status=204)

@app.errorhandler(404)
def not_found(error):
  return render_template("talk_not_found.html"), 404
