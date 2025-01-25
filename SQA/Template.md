## Test 1 `function name`
### Test ID: `Test ID`
### Method
```java
@Test
public void testAddInventory_Normal() {
	try {
		//here we had to use try catch because addInventory method can
		// throw InventoryException which is unhandled
		cm.addInventory("4","7","0","9"); //Coffee, Milk, Sugar, Chocolate
	} catch (InventoryException e) {
		//If any exception is thrown we manually fail the test case
		fail("InventoryException should not be thrown");
	}
	String inventory = cm.checkInventory();
	String expected = "Coffee: 19\nMilk: 22\nSugar: 15\nChocolate: 24\n";
	// We start with 15 in inventory, then added some.
	assertEquals(expected,inventory);
}
```

### Purpose
Some purpose text.......

### Execution Report: `PASSED`
