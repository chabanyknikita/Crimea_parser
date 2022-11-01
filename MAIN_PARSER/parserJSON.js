fetch('/JSON_CRIMEA/merged_file.json')
  .then((response) => response.json())
  .then((data) => {
    var emptyArr = []
    for (key in data) {
      let keyJSON = data[key]
      keyJSON.rate = +keyJSON.rate
      emptyArr.push(keyJSON)
    }
    console.log(data)
    emptyArr = emptyArr.sort((a, b) => {
      if (a.rate == b.rate) return 0
      if (a.rate < b.rate) return -1
      if (a.rate > b.rate) return 1
    })
    console.log(emptyArr)
    document.getElementById('arrayMessage').innerHTML = JSON.stringify(emptyArr)
  })
  .catch((error) => console.log(error))
