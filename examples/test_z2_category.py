# examples/test_z2_category.py

# To run this test, you must be in the main project directory (contrast-calculus)
# and execute: python -m examples.test_z2_category

# Now we can import our library components
from contrast_calculus import FusionCategory, get_z2_cocycle

def run_test():
    """Tests the Z_2 fusion category associator."""
    print("--- Running Z_2 Category Test ---")

    # 1. Get the cocycle function
    z2_cocycle = get_z2_cocycle()

    # 2. Define the group elements
    z2_group = [0, 1]

    # 3. Create an instance of our category
    category = FusionCategory(group_elements=z2_group, cocycle_function=z2_cocycle)
    print(f"Successfully created: {category}")

    # 4. Test the non-trivial associator value
    g1, g2, g3 = (1, 1, 1)
    associator_value = category.associator(g1, g2, g3)
    print(f"Associator for ({g1}, {g2}, {g3}) is: {associator_value}")

    # 5. Check if the result is correct
    assert associator_value == -1.0
    print("\n[SUCCESS] Test passed!")

if __name__ == "__main__":
    run_test()
