# Section 1 Project Overview: Must include a project title and summary paragraph explaining the application's purpose and its intended user.

**Spend Analyzer** is a data management and automation system that helps individuals understand their spending at grocery stores. The application ingests purchase data from grocery stores, normalizes inconsistent item and pricing information, and stores it in a structured database. Its intended users are individuals or households who want clearer insight into total spending, savings from discounts, and purchasing patterns without relying on bank aggregation tools or third-party budgeting apps.

## Section 2 Core Features: Must be a bulleted list defining the 3-5 essential user actions for the application.
- The User Will Be Able To:
- Import purchase history files from retailers (e.g., CSV or JSON exports)
- Build reports to identify spending trends like but not limited to: biggest location for savings, where most money is spent, forecast future pricing.
- Categorize the receipt uploaded like: grocery, retail, hobbies etc. Ideally this product will span beyond just       grocery stores.
- Generate automated weekly or monthly spending summaries by retailer and category

### Section 3 Data Model: Must define the structure of a single data record in your application, specifying fields and appropriate data types.
There will potentially be multiple tables to identify: store location, customer information, receipt information, etc. The most important table will be the one containing the individual item purchased. 

**Single Data Record: Line Item (Individual Purchased Item)**
- Example of one table that will contain the individual item purchased.
| Field Name             | Data Type        | Description                                       |
|------------------------|------------------|---------------------------------------------------|
| line_item_id           | Integer (PK)     | Unique identifier for the line item               |
| purchase_id            | Integer (FK)     | Identifier linking the item to a purchase/receipt |
| location_id            | Integer (FK)     | Identifier linking the item to a location         |
| item_description       | String           | Original item name as provided by the retailer    |
| item_normalized_name   | String           | Cleaned and standardized item name                |
| productupc             | String           | Store assigned value                              |
| unit_original_price    | Decimal          | Original per-unit price before discounts          |
| unit_paid_price        | Decimal          | Final per-unit price paid                         |
| line_total_paid        | Decimal          | Total amount paid for the item                    |
| line_total_savings     | Decimal          | Difference between original and paid price        |