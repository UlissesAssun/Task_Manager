import models.database as db
from view.view import menu

def main():
    db.init_database()
    menu()


if __name__ == "__main__":
    main()