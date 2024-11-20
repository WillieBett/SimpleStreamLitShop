import streamlit as st
import pandas as pd

# Sample product data for illustration
product_data = {
    'Product ID': [1, 2, 3],
    'Product Name': ['Shirt', 'Jeans', 'Jacket'],
    'Price': [500, 1000, 1500],
    'Stock': [100, 50, 30]
}

# Load the product data into a DataFrame
df = pd.DataFrame(product_data)

# Streamlit Dashboard
st.title("Shop Management System")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Product Management", "Sales Management", "Reports"])

if page == "Product Management":
    st.header("Manage Products")

    # Display product data
    st.subheader("Product List")
    st.dataframe(df)

    # Add new product
    st.subheader("Add New Product")
    with st.form(key="add_product_form"):
        new_id = st.number_input("Product ID", min_value=1)
        new_name = st.text_input("Product Name")
        new_price = st.number_input("Price", min_value=0)
        new_stock = st.number_input("Stock", min_value=0)
        submit_button = st.form_submit_button("Add Product")
        
        if submit_button:
            new_product = pd.DataFrame({'Product ID': [new_id], 'Product Name': [new_name], 'Price': [new_price], 'Stock': [new_stock]})
            df = pd.concat([df, new_product], ignore_index=True)
            st.success(f"Product '{new_name}' added successfully!")

elif page == "Sales Management":
    st.header("Sales Management")

    # Sales recording
    st.subheader("Record a Sale")
    product_list = df['Product Name'].tolist()
    selected_product = st.selectbox("Select Product", product_list)
    quantity_sold = st.number_input("Quantity Sold", min_value=1)
    
    submit_sale = st.button("Record Sale")
    
    if submit_sale:
        # Update the stock and display sale information
        product_index = df[df['Product Name'] == selected_product].index[0]
        updated_stock = df.at[product_index, 'Stock'] - quantity_sold
        
        if updated_stock < 0:
            st.warning("Not enough stock to record this sale!")
        else:
            df.at[product_index, 'Stock'] = updated_stock
            sale_amount = df.at[product_index, 'Price'] * quantity_sold
            st.success(f"Sale recorded! Amount: {sale_amount} for {quantity_sold} {selected_product}(s).")
            st.write(f"Updated Stock for {selected_product}: {updated_stock}")

elif page == "Reports":
    st.header("Sales Reports")

    # Display basic sales analytics (for now just display the product list and stock)
    st.subheader("Product Report")
    st.dataframe(df)
    
    # For advanced reporting, add charts and graphs (e.g., sales over time, most sold products)
    st.subheader("Sales Analytics")
    st.write("This section can include graphical representations of sales trends, stock levels, etc.")

# Run the app by executing the command: `streamlit run <your_file.py>`
