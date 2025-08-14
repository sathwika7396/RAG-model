#Initialize session state for vector store and chat history
if "vector" not in st.session state:
st.session state.vector= None
if "chat history" not in st.session state:
st.session state.chat_history = []
Sidebar for document upload
D
↑Top
with st.sidebar:
st.header("Upload Documents")
uploaded_files = st.file_uploader("Upload your PDF documents", type="pat", accept multiple_files=True)
LE
if st.button("Process Documents"):
if uploaded_files:
with st.spinner("Processing documents..."):
docs = []
for file in uploaded_files:
I
To read the file, we first write it to a temporary file
with open(file.name, "wb") as f:
f.write(file.getbuffer())
Loader PyPDFLoaderi file.name)
docs.extend(Loader.load())
E
K
Kumar Swamy
S

Stephen
