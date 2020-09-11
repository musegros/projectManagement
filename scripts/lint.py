import pylint.epylint

(stdout,stderr) = pylint.epylint.run('filename.py --msg-template='{msg_id} Line {line:3d}, column {column:2d}: {msg}"', return_std=True )
