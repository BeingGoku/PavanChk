import pymongo
from mongodb import usersdb, chats_auth, gcdb

def reset_mongodb():
    try:
        print("Starting MongoDB reset...")

        # Clear all user data
        result1 = usersdb.delete_many({})
        print(f"Deleted {result1.deleted_count} users from usersdb")

        # Clear all chat auth data
        result2 = chats_auth.delete_many({})
        print(f"Deleted {result2.deleted_count} chats from chats_auth")

        # Clear all gift code data
        result3 = gcdb.delete_many({})
        print(f"Deleted {result3.deleted_count} gift codes from gcdb")

        print("MongoDB reset completed successfully! ✅")
        print("All user data, chat authorizations, and gift codes have been cleared.")
        print("You can now start fresh with your bot.")

    except Exception as e:
        print(f"Error resetting MongoDB: {e}")

if __name__ == "__main__":
    confirmation = input("Are you sure you want to reset MongoDB? This will delete ALL data! (yes/no): ")
    if confirmation.lower() == "yes":
        reset_mongodb()
    else:
        print("MongoDB reset cancelled.")