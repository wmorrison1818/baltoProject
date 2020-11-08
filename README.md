# Will Morrison
For my project I used a React frontend with a Flask backend and a sqlite database. I used React as you requested. I used Flask and sqlite because I was a bit familiar with them already, and they are very easy to use given the time constraint. I used a template to start with for my React frontend which is located in the “WebFrontEnd” folder which contains a readme about where it came from. Other than that template I just used documentation from the various libraries and frameworks.

I would also ask that you view my 1 closed PR on this repo to see how I document my pull requests.

See the below information for descriptions on the data processing I did on the csv.

Thank you for your consideration,

Will


```python
import pandas as pd
import sqlite3
import uuid
```

## Data Processing
I used pandas for most of my data processing and to ingest the csv as you requested. 


```python
con = sqlite3.connect("movieData.sqlite")
cur = con.cursor()
```


```python
moviesDf = pd.read_csv("movie_plots.csv")
moviesDf
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Release Year</th>
      <th>Title</th>
      <th>Origin/Ethnicity</th>
      <th>Director</th>
      <th>Cast</th>
      <th>Genre</th>
      <th>Wiki Page</th>
      <th>Plot</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1901</td>
      <td>Kansas Saloon Smashers</td>
      <td>American</td>
      <td>Unknown</td>
      <td>NaN</td>
      <td>unknown</td>
      <td>https://en.wikipedia.org/wiki/Kansas_Saloon_Sm...</td>
      <td>A bartender is working at a saloon, serving dr...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1901</td>
      <td>Love by the Light of the Moon</td>
      <td>American</td>
      <td>Unknown</td>
      <td>NaN</td>
      <td>unknown</td>
      <td>https://en.wikipedia.org/wiki/Love_by_the_Ligh...</td>
      <td>The moon, painted with a smiling face hangs ov...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1901</td>
      <td>The Martyred Presidents</td>
      <td>American</td>
      <td>Unknown</td>
      <td>NaN</td>
      <td>unknown</td>
      <td>https://en.wikipedia.org/wiki/The_Martyred_Pre...</td>
      <td>The film, just over a minute long, is composed...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1901</td>
      <td>Terrible Teddy, the Grizzly King</td>
      <td>American</td>
      <td>Unknown</td>
      <td>NaN</td>
      <td>unknown</td>
      <td>https://en.wikipedia.org/wiki/Terrible_Teddy,_...</td>
      <td>Lasting just 61 seconds and consisting of two ...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1902</td>
      <td>Jack and the Beanstalk</td>
      <td>American</td>
      <td>George S. Fleming, Edwin S. Porter</td>
      <td>NaN</td>
      <td>unknown</td>
      <td>https://en.wikipedia.org/wiki/Jack_and_the_Bea...</td>
      <td>The earliest known adaptation of the classic f...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>34881</th>
      <td>2014</td>
      <td>The Water Diviner</td>
      <td>Turkish</td>
      <td>Director: Russell Crowe</td>
      <td>Director: Russell Crowe\r\nCast: Russell Crowe...</td>
      <td>unknown</td>
      <td>https://en.wikipedia.org/wiki/The_Water_Diviner</td>
      <td>The film begins in 1919, just after World War ...</td>
    </tr>
    <tr>
      <th>34882</th>
      <td>2017</td>
      <td>Çalgı Çengi İkimiz</td>
      <td>Turkish</td>
      <td>Selçuk Aydemir</td>
      <td>Ahmet Kural, Murat Cemcir</td>
      <td>comedy</td>
      <td>https://en.wikipedia.org/wiki/%C3%87alg%C4%B1_...</td>
      <td>Two musicians, Salih and Gürkan, described the...</td>
    </tr>
    <tr>
      <th>34883</th>
      <td>2017</td>
      <td>Olanlar Oldu</td>
      <td>Turkish</td>
      <td>Hakan Algül</td>
      <td>Ata Demirer, Tuvana Türkay, Ülkü Duru</td>
      <td>comedy</td>
      <td>https://en.wikipedia.org/wiki/Olanlar_Oldu</td>
      <td>Zafer, a sailor living with his mother Döndü i...</td>
    </tr>
    <tr>
      <th>34884</th>
      <td>2017</td>
      <td>Non-Transferable</td>
      <td>Turkish</td>
      <td>Brendan Bradley</td>
      <td>YouTubers Shanna Malcolm, Shira Lazar, Sara Fl...</td>
      <td>romantic comedy</td>
      <td>https://en.wikipedia.org/wiki/Non-Transferable...</td>
      <td>The film centres around a young woman named Am...</td>
    </tr>
    <tr>
      <th>34885</th>
      <td>2017</td>
      <td>İstanbul Kırmızısı</td>
      <td>Turkish</td>
      <td>Ferzan Özpetek</td>
      <td>Halit Ergenç, Tuba Büyüküstün, Mehmet Günsür, ...</td>
      <td>romantic</td>
      <td>https://en.wikipedia.org/wiki/%C4%B0stanbul_K%...</td>
      <td>The writer Orhan Şahin returns to İstanbul aft...</td>
    </tr>
  </tbody>
</table>
<p>34886 rows × 8 columns</p>
</div>



I did some light data processing. I changed the column names to be a bit more friendly to coding and I added a UID.


```python
mRename = moviesDf.rename(columns={"Release Year": "ReleaseYear", "Origin/Ethnicity": "Origin", "Wiki Page": "WikiPage"})
```


```python
mRename['id'] = [uuid.uuid4() for _ in range(len(mRename.index))]
mRename['id']= mRename['id'].astype('str')
mRename
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ReleaseYear</th>
      <th>Title</th>
      <th>Origin</th>
      <th>Director</th>
      <th>Cast</th>
      <th>Genre</th>
      <th>WikiPage</th>
      <th>Plot</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1901</td>
      <td>Kansas Saloon Smashers</td>
      <td>American</td>
      <td>Unknown</td>
      <td>NaN</td>
      <td>unknown</td>
      <td>https://en.wikipedia.org/wiki/Kansas_Saloon_Sm...</td>
      <td>A bartender is working at a saloon, serving dr...</td>
      <td>ac8044ff-7093-4935-aff9-678d3ddfa075</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1901</td>
      <td>Love by the Light of the Moon</td>
      <td>American</td>
      <td>Unknown</td>
      <td>NaN</td>
      <td>unknown</td>
      <td>https://en.wikipedia.org/wiki/Love_by_the_Ligh...</td>
      <td>The moon, painted with a smiling face hangs ov...</td>
      <td>92420e92-a871-4948-936c-eff0ce18a55d</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1901</td>
      <td>The Martyred Presidents</td>
      <td>American</td>
      <td>Unknown</td>
      <td>NaN</td>
      <td>unknown</td>
      <td>https://en.wikipedia.org/wiki/The_Martyred_Pre...</td>
      <td>The film, just over a minute long, is composed...</td>
      <td>005118ac-2b80-4d1f-8dd8-57618e561fc3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1901</td>
      <td>Terrible Teddy, the Grizzly King</td>
      <td>American</td>
      <td>Unknown</td>
      <td>NaN</td>
      <td>unknown</td>
      <td>https://en.wikipedia.org/wiki/Terrible_Teddy,_...</td>
      <td>Lasting just 61 seconds and consisting of two ...</td>
      <td>3d1a42ef-ca75-4e11-aa53-b1b04068d8ff</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1902</td>
      <td>Jack and the Beanstalk</td>
      <td>American</td>
      <td>George S. Fleming, Edwin S. Porter</td>
      <td>NaN</td>
      <td>unknown</td>
      <td>https://en.wikipedia.org/wiki/Jack_and_the_Bea...</td>
      <td>The earliest known adaptation of the classic f...</td>
      <td>653e1500-a8a5-41b1-bb50-f15bf7961fa5</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>34881</th>
      <td>2014</td>
      <td>The Water Diviner</td>
      <td>Turkish</td>
      <td>Director: Russell Crowe</td>
      <td>Director: Russell Crowe\r\nCast: Russell Crowe...</td>
      <td>unknown</td>
      <td>https://en.wikipedia.org/wiki/The_Water_Diviner</td>
      <td>The film begins in 1919, just after World War ...</td>
      <td>793ba238-5f6e-488d-a728-8c8b113a7985</td>
    </tr>
    <tr>
      <th>34882</th>
      <td>2017</td>
      <td>Çalgı Çengi İkimiz</td>
      <td>Turkish</td>
      <td>Selçuk Aydemir</td>
      <td>Ahmet Kural, Murat Cemcir</td>
      <td>comedy</td>
      <td>https://en.wikipedia.org/wiki/%C3%87alg%C4%B1_...</td>
      <td>Two musicians, Salih and Gürkan, described the...</td>
      <td>b84af0ac-f74d-435d-b56b-16f90ff8dedc</td>
    </tr>
    <tr>
      <th>34883</th>
      <td>2017</td>
      <td>Olanlar Oldu</td>
      <td>Turkish</td>
      <td>Hakan Algül</td>
      <td>Ata Demirer, Tuvana Türkay, Ülkü Duru</td>
      <td>comedy</td>
      <td>https://en.wikipedia.org/wiki/Olanlar_Oldu</td>
      <td>Zafer, a sailor living with his mother Döndü i...</td>
      <td>69e80286-227f-444f-abc3-4dc747fd2c46</td>
    </tr>
    <tr>
      <th>34884</th>
      <td>2017</td>
      <td>Non-Transferable</td>
      <td>Turkish</td>
      <td>Brendan Bradley</td>
      <td>YouTubers Shanna Malcolm, Shira Lazar, Sara Fl...</td>
      <td>romantic comedy</td>
      <td>https://en.wikipedia.org/wiki/Non-Transferable...</td>
      <td>The film centres around a young woman named Am...</td>
      <td>e9a8d50c-99b6-4336-b67c-c395b352c98b</td>
    </tr>
    <tr>
      <th>34885</th>
      <td>2017</td>
      <td>İstanbul Kırmızısı</td>
      <td>Turkish</td>
      <td>Ferzan Özpetek</td>
      <td>Halit Ergenç, Tuba Büyüküstün, Mehmet Günsür, ...</td>
      <td>romantic</td>
      <td>https://en.wikipedia.org/wiki/%C4%B0stanbul_K%...</td>
      <td>The writer Orhan Şahin returns to İstanbul aft...</td>
      <td>907d4bcb-fd6c-4ba7-be84-b80e870d137f</td>
    </tr>
  </tbody>
</table>
<p>34886 rows × 9 columns</p>
</div>




```python
mRename.to_sql("movie", con, index=False)
```


```python
movieData = pd.read_sql_query("SELECT * from movie", con)
movieData
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ReleaseYear</th>
      <th>Title</th>
      <th>Origin</th>
      <th>Director</th>
      <th>Cast</th>
      <th>Genre</th>
      <th>WikiPage</th>
      <th>Plot</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1901</td>
      <td>Kansas Saloon Smashers</td>
      <td>American</td>
      <td>Unknown</td>
      <td>None</td>
      <td>unknown</td>
      <td>https://en.wikipedia.org/wiki/Kansas_Saloon_Sm...</td>
      <td>A bartender is working at a saloon, serving dr...</td>
      <td>ac8044ff-7093-4935-aff9-678d3ddfa075</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1901</td>
      <td>Love by the Light of the Moon</td>
      <td>American</td>
      <td>Unknown</td>
      <td>None</td>
      <td>unknown</td>
      <td>https://en.wikipedia.org/wiki/Love_by_the_Ligh...</td>
      <td>The moon, painted with a smiling face hangs ov...</td>
      <td>92420e92-a871-4948-936c-eff0ce18a55d</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1901</td>
      <td>The Martyred Presidents</td>
      <td>American</td>
      <td>Unknown</td>
      <td>None</td>
      <td>unknown</td>
      <td>https://en.wikipedia.org/wiki/The_Martyred_Pre...</td>
      <td>The film, just over a minute long, is composed...</td>
      <td>005118ac-2b80-4d1f-8dd8-57618e561fc3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1901</td>
      <td>Terrible Teddy, the Grizzly King</td>
      <td>American</td>
      <td>Unknown</td>
      <td>None</td>
      <td>unknown</td>
      <td>https://en.wikipedia.org/wiki/Terrible_Teddy,_...</td>
      <td>Lasting just 61 seconds and consisting of two ...</td>
      <td>3d1a42ef-ca75-4e11-aa53-b1b04068d8ff</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1902</td>
      <td>Jack and the Beanstalk</td>
      <td>American</td>
      <td>George S. Fleming, Edwin S. Porter</td>
      <td>None</td>
      <td>unknown</td>
      <td>https://en.wikipedia.org/wiki/Jack_and_the_Bea...</td>
      <td>The earliest known adaptation of the classic f...</td>
      <td>653e1500-a8a5-41b1-bb50-f15bf7961fa5</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>34881</th>
      <td>2014</td>
      <td>The Water Diviner</td>
      <td>Turkish</td>
      <td>Director: Russell Crowe</td>
      <td>Director: Russell Crowe\r\nCast: Russell Crowe...</td>
      <td>unknown</td>
      <td>https://en.wikipedia.org/wiki/The_Water_Diviner</td>
      <td>The film begins in 1919, just after World War ...</td>
      <td>793ba238-5f6e-488d-a728-8c8b113a7985</td>
    </tr>
    <tr>
      <th>34882</th>
      <td>2017</td>
      <td>Çalgı Çengi İkimiz</td>
      <td>Turkish</td>
      <td>Selçuk Aydemir</td>
      <td>Ahmet Kural, Murat Cemcir</td>
      <td>comedy</td>
      <td>https://en.wikipedia.org/wiki/%C3%87alg%C4%B1_...</td>
      <td>Two musicians, Salih and Gürkan, described the...</td>
      <td>b84af0ac-f74d-435d-b56b-16f90ff8dedc</td>
    </tr>
    <tr>
      <th>34883</th>
      <td>2017</td>
      <td>Olanlar Oldu</td>
      <td>Turkish</td>
      <td>Hakan Algül</td>
      <td>Ata Demirer, Tuvana Türkay, Ülkü Duru</td>
      <td>comedy</td>
      <td>https://en.wikipedia.org/wiki/Olanlar_Oldu</td>
      <td>Zafer, a sailor living with his mother Döndü i...</td>
      <td>69e80286-227f-444f-abc3-4dc747fd2c46</td>
    </tr>
    <tr>
      <th>34884</th>
      <td>2017</td>
      <td>Non-Transferable</td>
      <td>Turkish</td>
      <td>Brendan Bradley</td>
      <td>YouTubers Shanna Malcolm, Shira Lazar, Sara Fl...</td>
      <td>romantic comedy</td>
      <td>https://en.wikipedia.org/wiki/Non-Transferable...</td>
      <td>The film centres around a young woman named Am...</td>
      <td>e9a8d50c-99b6-4336-b67c-c395b352c98b</td>
    </tr>
    <tr>
      <th>34885</th>
      <td>2017</td>
      <td>İstanbul Kırmızısı</td>
      <td>Turkish</td>
      <td>Ferzan Özpetek</td>
      <td>Halit Ergenç, Tuba Büyüküstün, Mehmet Günsür, ...</td>
      <td>romantic</td>
      <td>https://en.wikipedia.org/wiki/%C4%B0stanbul_K%...</td>
      <td>The writer Orhan Şahin returns to İstanbul aft...</td>
      <td>907d4bcb-fd6c-4ba7-be84-b80e870d137f</td>
    </tr>
  </tbody>
</table>
<p>34886 rows × 9 columns</p>
</div>




```python
con.close()
```
