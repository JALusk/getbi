import unittest

from dot20parser import Dot20Parser

class ConstructorTestCase(unittest.TestCase):
  def setUp(self):
    self.model_name   = 'fakemodelname'
    self.model_number = 'fakemodelnumber'
    self.file_path    = '/fake/file/path'

    self.parser = Dot20Parser(self.model_name, self.model_number, self.file_path)

class ConstructorModelNameTestCase(ConstructorTestCase):
  def runTest(self):
    self.assertEqual(self.model_name, self.parser.model_name)

class ConstructorModelNumberTestCase(ConstructorTestCase):
  def runTest(self):
    self.assertEqual(self.model_number, self.parser.model_number)

class ConstructorFilePathTestCase(ConstructorTestCase):
  def runTest(self):
    self.assertEqual(self.file_path, self.parser.file_path)

#class Dot20ParserFileHandleTestCase(unittest.TestCase):
#class Dot20ParserFileContentsTestCase(unittest.TestCase):
#class Dot20ParserCloseFileHandleTestCase(unittest.TestCase):
