default_config = {"host": "localhost", "port": 5432}
custom_config = {"dbname": "testdb", "user": "postgres"}

final_config = {**default_config, **custom_config}
print(final_config)

# This code merges two dictionaries, `default_config` and `custom_config`, into a new dictionary called `final_config`.
# The `**` operator is used to unpack the key-value pairs from both dictionaries.
# The resulting `final_config` dictionary will contain all the keys from both dictionaries, with values from `custom_config` overriding those in `default_config` if there are any conflicts.