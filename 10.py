from json import load
from os.path import dirname

__config = load(open(r"{0}\config.json".format(dirname(__file__))))

#-----#

exec(open(r"{0}\__main__.py".format(dirname(__file__))).read())

Bot.run(
	__config["User"]["10"]["E-Mail"],
	__config["User"]["10"]["Password"]
	)