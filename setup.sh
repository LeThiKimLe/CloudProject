mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"20110248@student.hcmute.edu.vn\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml