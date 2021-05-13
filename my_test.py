import unittest
import my
import sqlite3

class TestMy(unittest.TestCase):
    # run before every test case.
    def setUp(self):
        self.con = sqlite3.connect(":memory:")
        cur = self.con.cursor()
        
        # this is one benefit of having a 'schema file'.
        # You can share the schema with your test code.
        with open("my.schema") as f: 
            schema = ''.join(f.readlines())
            cur.executescript(schema)
        users = [
            (1, "Brandon"),
            (2, "Liam"),
            (3, "Natasha")
        ]
        posts = [
            (1, 1, "I hate turnips!"),
            (2, 3, "I love carrots!"),
            (3, 2, "I love dark souls!"),
            (4, 1, "I love potatoes!"),
        ]
        
        # throw some junk values into our DB
        for user in users:  
            cur.execute("INSERT INTO users values(?, ?)", user) 
        for post in posts:  
            cur.execute("INSERT INTO posts values(?, ?, ?)", post)
        self.con.commit()
        
    def test_rowcount(self):
        self.assertEqual(my.post_count(self.con, 1), 2)
        self.assertEqual(my.post_count(self.con, 2), 1)
        self.assertEqual(my.post_count(self.con, 4), 0)

if __name__ == '__main__':
    unittest.main()