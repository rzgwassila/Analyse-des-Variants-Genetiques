import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data (Updated to use st.cache_data)
@st.cache_data
def load_data():
    fact = pd.read_csv('fact_variants.csv')
    dim_disease = pd.read_csv('dim_disease.csv')
    dim_genome = pd.read_csv('dim_genome.csv')
    dim_clinical = pd.read_csv('dim_clinical.csv')
    
    return fact, dim_disease, dim_genome, dim_clinical

fact, dim_disease, dim_genome, dim_clinical = load_data()

# Merge fact table with dimension tables
fact_table = fact.merge(dim_disease, on='disease_id', how='left')
fact_table = fact_table.merge(dim_genome, on='genome_id', how='left')
fact_table = fact_table.merge(dim_clinical, on='clinical_id', how='left')

# Sidebar for user input
st.sidebar.title("OLAP Operations")
operation = st.sidebar.radio("Choose OLAP Operation", ['Roll-up', 'Drill-down', 'Slice', 'Dice'])

if operation == 'Roll-up':
    st.header("Roll-up: Aggregation by Disease")
    # Aggregating variants count by disease
    rollup = fact_table.groupby('disease_name').size().reset_index(name='variant_count')
    st.write(rollup)
    
    # Visualize
    st.subheader("Bar Chart of Variant Counts by Disease")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=rollup, x='disease_name', y='variant_count', palette='muted', ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    st.pyplot(fig)

elif operation == 'Drill-down':
    st.header("Drill-down: Detail View by Disease and Genome Position")
    # Drill down by disease and genome position
    drilldown = fact_table[['disease_name', 'chrom', 'pos', 'ref', 'alt']]
    st.write(drilldown)

elif operation == 'Slice':
    st.header("Slice: Filter by Disease")
    disease = st.selectbox('Select a disease to filter:', fact_table['disease_name'].unique())
    slice_df = fact_table[fact_table['disease_name'] == disease]
    st.write(slice_df)
    
    # Visualize slice by disease
    st.subheader(f"Variant Counts for {disease}")
    slice_rollup = slice_df.groupby('disease_name').size().reset_index(name='variant_count')
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=slice_rollup, x='disease_name', y='variant_count', palette='viridis', ax=ax)
    st.pyplot(fig)

elif operation == 'Dice':
    st.header("Dice: Filter by Multiple Dimensions")
    disease = st.selectbox('Select a disease to filter:', fact_table['disease_name'].unique())
    chrom = st.selectbox('Select a chromosome to filter:', fact_table['chrom'].unique())
    
    dice_df = fact_table[(fact_table['disease_name'] == disease) & (fact_table['chrom'] == chrom)]
    st.write(dice_df)
    
    # Visualize dice
    st.subheader(f"Variant Counts for {disease} on Chromosome {chrom}")
    dice_rollup = dice_df.groupby('disease_name').size().reset_index(name='variant_count')
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=dice_rollup, x='disease_name', y='variant_count', palette='Blues', ax=ax)
    st.pyplot(fig)

# Option to display full data
if st.sidebar.checkbox("Show Full Fact Table"):
    st.subheader("Full Fact Table")
    st.write(fact_table)