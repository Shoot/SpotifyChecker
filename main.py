import os
import time
import logging
from spotify import Checker

logging.basicConfig(
	level=logging.INFO,
	format="[%(asctime)s] [%(threadName)s] %(levelname)s: %(message)s",
	datefmt="%H:%M:%S"
)

log = logging.getLogger(__name__)

if __name__ == "__main__":
	if not os.path.isfile('list.txt'):
		raise Exception('Please create the `list.txt` file.')

	with open('list.txt', 'r', encoding='utf-8') as file:
		list = file.read().split('\n')

	checker = Checker()

	out = open('out ' + str(int(time.time())) + '.txt', 'a', encoding='utf-8')

	for account in list:
		us, pw = tuple(account.split(':'))
		result = checker.check(us, pw)

		log.info('Checking ' + account)
		if result:
			out.write(us + '\n')

	out.close()

	log.info('Finished')