package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
)

func main() {

	url := "https://catalogue.iudx.org.in/catalogue/v1/search?geometry=linestring%2818.56,73.83,18.49,73.8%29&relation=intersects"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}