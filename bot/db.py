import sqlite3
import logging

connection = sqlite3.connect("db/ling")


class Problem:
    def __init__(self, user_vk_id: int, text: str, rang: str,
                 tags: [str]) -> None:
        self.user_vk_id = user_vk_id
        self.text = text
        self.rang = rang
        self.tags = tags

    def execute(self) -> None:
        try:
            connection.execute("""
            insert into Problems(Comment, User, Rang) values
            (?, (select id from User where VK_ID=?),
            (select id from Rangs where RangValue=?))
            """, (self.text, self.user_vk_id, self.rang.strip()))

            current_id = connection.execute("""
                select last_insert_rowid()
            """)

            for tag in self.tags:
                connection.execute("""
                    insert into Problems_Tag(Problem_ID, Tag_ID) values 
                    (?, (select id from Tags where TagValue=?))
                """, (current_id.lastrowid, tag.strip()))

            connection.commit()

        except sqlite3.OperationalError as error:
            logging.error("cannot connect " + str(self) +
                          ' because ' + str(error))
        except sqlite3.IntegrityError as error:
            logging.error("cannot execute " + str(self) +
                          ' because ' + str(error))

    def __str__(self):
        return "Problem(%s, %s, %s, %s)" \
               % (self.user_vk_id, self.text, self.rang, self.tags)


class User:
    def __init__(self, vk_id: int) -> None:
        self.vk_id = vk_id
        self.id = None

    def init_if_exists(self) -> bool:
        try:
            user = connection.execute("""
                select ID, VK_ID from User where VK_ID=?
            """, (self.vk_id,))

            result = user.fetchone()
            if result is None:
                return False

            self.id = result[0]

            return True

        except sqlite3.OperationalError as error:
            logging.error("cannot connect " + str(self) +
                          ' because ' + str(error))
        except sqlite3.IntegrityError as error:
            logging.error("cannot execute " + str(self) +
                          ' because ' + str(error))

        return False

    def __str__(self) -> str:
        return "User(%s, %s)" % (self.id, self.vk_id)

    def execute_if_not_exists(self):
        if not self.init_if_exists():
            self.execute()

    def execute(self):
        try:
            connection.execute("""
                insert into User(VK_ID) values (?)
            """, (self.vk_id,))

            self.id = connection\
                .execute("""select last_insert_rowid()""").lastrowid

            connection.commit()

        except sqlite3.OperationalError as error:
            logging.error("cannot connect " + str(self) +
                          ' because ' + str(error))
        except sqlite3.IntegrityError as error:
            logging.error("cannot execute " + str(self) +
                          ' because ' + str(error))


class Document:
    def __init__(self):
        self.name = None
        self.surname = None
        self.parent_name = None
        self.group = None
        self.id = None

    def get_from_id(self, idd: int) -> bool:
        if self.id is not None:
            return False

        try:
            document = connection.execute("""
                select Surname, Name, ParentName,`Group` from DocumentRequests
                where ID=?
            """, (idd,)).fetchone()

            if document is None:
                return False

            self.name = document[1]
            self.surname = document[0]
            self.parent_name = document[2]
            self.group = document[3]
            self.id = idd

            return True

        except sqlite3.OperationalError as error:
            logging.error("cannot connect " + str(self) +
                          ' because ' + str(error))
        except sqlite3.IntegrityError as error:
            logging.error("cannot execute " + str(self) +
                          ' because ' + str(error))

        return False

    def create(self, surname: str, name: str, parent_name: str, group: str)\
            -> None:
        if self.id is not None:
            return

        try:
            connection.execute("""
                insert into DocumentRequests(Surname, Name, ParentName, "Group")
                values (?, ?, ?, ?)
            """, (surname, name, parent_name, group,))

            self.id = connection\
                .execute("""select last_insert_rowid()""").lastrowid

            self.group = group
            self.parent_name = parent_name
            self.name = name
            self.surname = self.surname

            connection.commit()

        except sqlite3.OperationalError as error:
            logging.error("cannot connect " + str(self) +
                          ' because ' + str(error))
        except sqlite3.IntegrityError as error:
            logging.error("cannot execute " + str(self) +
                          ' because ' + str(error))

    def __str__(self) -> str:
        return "Document(%s, %s, %s, %s)" % (self.surname, self.name,
                                             self.parent_name, self.group)

    def delete(self):
        if self.id is None:
            raise AssertionError("cannot delete None")

        try:
            connection.execute("""
                delete from DocumentRequests where ID=?
            """, (self.id,))

            connection.commit()

        except sqlite3.OperationalError as error:
            logging.error("cannot connect " + str(self) +
                          ' because ' + str(error))
        except sqlite3.IntegrityError as error:
            logging.error("cannot execute " + str(self) +
                          ' because ' + str(error))

