var settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://catalogue.iudx.org.in/catalogue/v1/count?attribute-name=%28tags%29&attribute-value=%28traffic%29&lat=12.273737&lon=78.37475&radius=200000",
    "method": "GET",
  }
  
  $.ajax(settings).done(function (response) {
    console.log(response);
  });