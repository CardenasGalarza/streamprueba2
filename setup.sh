mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"alex10estadistica@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[theme]\n\
base='light'\n\
primaryColor='#3a70ec'\n\
backgroundColor='#4359de'\n\
secondaryBackgroundColor = '#F0F2F6'\n\
textColor='#0e1862'\n\
font = 'sans serif'\n\

[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml