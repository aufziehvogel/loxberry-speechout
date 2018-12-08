pluginfoldername=$3

cp /opt/loxberry/data/plugins/$pluginfoldername/supervisor.conf /etc/supervisor/conf.d/texttospeech.conf

supervisorctl reread
supervisorctl reload
supervisorctl start texttospeech
