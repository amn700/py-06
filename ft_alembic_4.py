import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print("Now show that not all functions can be reached")
print("This will raise an exception!")
print("Testing the hidden create_earth: ", end="", flush=True)
try:
	print(f"{alchemy.create_earth()}")
except AttributeError as exc:
	print(f"{exc.__class__.__name__}: {exc}")
