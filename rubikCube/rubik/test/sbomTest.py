'''
Created on Jan 18, 2023

@author: bmm0066
'''
import unittest
import app


class sbomTest(unittest.TestCase):


    def test_sbom_100_ShouldReturnAuthorName(self):
        myName = 'bmm0066'
        result = app._getAuthor('../../')
        resultingAuthorName = result['author']
        self.assertEqual(resultingAuthorName, myName)
