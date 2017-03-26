import flask
import subprocess
import re

app = flask.Flask(__name__)

stored_volume = None

@app.route('/say', methods=['GET', 'POST'])
def say():
	text = flask.request.values.get('text')

	# TODO: Make language configurable
        # TODO: Then this replace should only happen for German
        # replace a dot in numeric expressions with a comma
        text = re.sub('(\d+)\.(\d+)', '\\1,\\2', text)

	tmpfile = '/tmp/out.wav'
	subprocess.call(['pico2wave', '-w', tmpfile, '-l', 'de-DE', text])
	subprocess.call(['aplay', tmpfile])
	
	return flask.jsonify({"status", "OK"})

@app.route('/volume_up/<int:level>')
def volume_up(level):
	subprocess.call(['amixer', 'sset', 'PCM', str(level) + '+'])
	return flask.jsonify({"status": "OK"})

@app.route('/volume_down/<int:level>')
def volume_down(level):
	subprocess.call(['amixer', 'sset', 'PCM', str(level) + '-'])
	return flask.jsonify({"status": "OK"})

@app.route('/volume_set')
def volume_set():
	level = flask.request.args.get('level')
	subprocess.call(['amixer', 'sset', 'PCM', level + '%'])
	return flask.jsonify({"status": "OK"})

@app.route('/volume_store')
def volume_store():
	global stored_volume

	res = subprocess.check_output(['amixer', 'get', 'PCM'])
	for line in res.splitlines():
		m = re.search(r'\[(\d+)\%\]', line)
		if m is not None:
			stored_volume = m.group(1)
	
	return flask.jsonify({"status": "OK"})

@app.route('/volume_restore')
def volume_restore():
	global stored_volume

	if stored_volume is not None:
		subprocess.call(['amixer', 'sset', 'PCM', str(stored_volume) + '%'])
	
	return flask.jsonify({"status": "OK"})
