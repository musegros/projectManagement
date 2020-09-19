#!/usr/bin/python3
import os
import sys

# This adds the virtual environment's `site-packages` to your path.  Note
# it is setting the path relative to the location of this script, which I assume
# is one directory into your project (in a folder called `scripts`, say)
script_path = os.path.dirname( os.path.realpath( __file__ ) )
sys.path.insert(1, os.path.join( script_path, ".."))
sys.path.insert(1, os.path.join( script_path, '../activityTwo/lib/python3.8/site-packages' ) )

import unittest
import hello
import unittest.mock
import pylint.epylint

class CoinTossTester(unittest.TestCase):
	def test_heads(self):
		with unittest.mock.patch('random.randint', side_effect=[0]) as mock_randint:
			self.assertEqual( hello.coin_toss(), 'Heads' )

	def test_tails(self):
		with unittest.mock.patch('random.randint', side_effect=[1]) as mock_randint:
			self.assertEqual( hello.coin_toss(), 'Tails' )

if __name__ == '__main__':
	passes_checks = True
	runner = unittest.TextTestRunner()
	results = runner.run(unittest.makeSuite(CoinTossTester))

	if len(results.errors) > 0 or len(results.failures) > 0:
		print('Something went wrong so you should exit with non-zero')
		print(results.errors)
		print(results.failures)
		passes_checks = False
																			
	(stdout, stderr) = pylint.epylint.py_run('hello.py --msg-template="{msg_id} ' +\
			'Line {line:3d}, column {column:2d}: {msg}"', return_std=True )

	pylint_checks = ["C0301", "C0303", "E0213", "C0102", "E0211", "W0312"]

	stdoutLines = stdout.getvalue()


	for line in stdout.getvalue().split('\n'):
		if len(line.split()) > 0 and line.split()[0] in pylint_checks:
			passes_checks = False
			print(line)

	if not passes_checks:
		sys.exit(1)
	
