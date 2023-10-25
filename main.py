from fastapi import FastAPI
import uvicorn
import source_code

app=FastAPI()

@app.get('/')
async def msg():
    return 'Server alive'

@app.get('/moviename/{movie}')
async def recommend(movie):
    try:
        recommendation=source_code.recommended(movie)
        return recommendation
    except:
        return 'Recommendation not available'

if __name__=='__main__':
    uvicorn.run(app, host='localhost', port=8002)