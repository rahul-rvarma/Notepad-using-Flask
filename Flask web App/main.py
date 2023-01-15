from website import create_app

app = create_app()

if __name__=='__main__':
    app.run(debug=True)
    #rerun everytime when a code is changed in the application)
    
    