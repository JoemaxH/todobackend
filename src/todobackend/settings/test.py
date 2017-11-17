from base import *
import os

#INSTALLED APPS

INSTALLED_APPS += ('django_nose', )
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
TEST_OUTPUT_DIR = os.environ.get('TEST_OUTPUT_DIR','.')
NOSE_ARGS = [
	'--verbosity=2',					#verbose output
	'--nologcapture', 				#don't output log capture
	'--with-coverage',				#activate coverage report
	'--cover-package=todo',			#coverage reports will apply to these packages
	'--with-spec',					#spec style tests
	'--spec-color',
	'--with-xunit',
	'--xunit-file=%s/unittests.xml' % TEST_OUTPUT_DIR,
	'--cover-xml',
	'--cover-xml-file=%s/coverage.xml' % TEST_OUTPUT_DIR,
]

#DATABASE
#https://docs.djangoproject.com/en/1.8/ref/settings/#datavases
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': os.environ.get('MYSQL_DATABASE', 'todobackend'),
		'USER': os.environ.get('MYSQL_USER', 'todo'),
		'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'Password*$3'),
		'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
		'PORT': os.environ.get('MYSQL_PORT', '3306'),
	}
}