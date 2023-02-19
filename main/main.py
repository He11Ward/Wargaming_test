from create_db import CreationDb


if __name__ == "__main__":
    """
    used to create db
    """
    CreationDb.create_db()

    # feel free to start testing from here or with python -m pytest
    from pytest import main
    main(['../tests/test_db.py'])
