#impoort libraries
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image



#page title
image=Image.open('dna-5695421_1920.jpg')
st.image(image,use_column_width=True)
st.write("""
# K-mer Counting Web App

This is app to find appropriate K-mer

***
""")


#Input Text Box Seqence
st.header('Enter DNA Seqence')
sequence_input=">DNA\nAGGGGGGGGGGTTTCCCAACGAACCCCCCCAGGGATGTGTAGTGACTAGTAGTGATGTAGTAGATGAGTAGTAACACCCAATTTTTTTTTTTTTTT";
seqence=st.text_area("sequence input ",sequence_input,height=25)
seqence=seqence.splitlines()
seqence=seqence[1:]
seqence=''.join(seqence)
st.write("""
***
""")

#Input Slider k-mer
kmer_input="Enter K Length"
kmer=st.slider("enter k length",0,100,1)

st.write("""
***
""")

#Display DNA Input without first line
st.header("Input DNA Query")
seqence

st.write("""
***
""");

#NUMBER OF K-MER
S=len(seqence)-kmer+1
st.header("#NUMBER OF K-MER:")
st.header(S)

#The number of times each K-mer is repeated in the DNA sequences
def kmers(seq,k):
    k_dictionary={}
    for i in range(0,len(seq)-k+1):
        KMER=seq[i:i+k];
        if KMER in k_dictionary:
            k_dictionary [KMER]+=1
        else:
            k_dictionary[KMER] = 1

    return k_dictionary
dec=kmers(seqence,kmer)





#Display DataFrame in table
st.header('3.Display DataFrame')
df=pd.DataFrame.from_dict(dec,orient='index')
df=df.rename({0:'count'},axis='columns')
df.reset_index(inplace=True)
df=df.rename(columns={'index':'KMERS'})





st.write(df)


#Display Bar chart
st.subheader('4.Display Bar chart')
p=alt.Chart(df).mark_bar().encode(
    x='KMERS',
    y='count'
)
p=p.properties(
    width=alt.Step(12)
)
st.write(p)