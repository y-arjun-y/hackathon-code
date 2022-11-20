const express = require("express");
const app = express();
const path = require("path");

const port = 3000;

app.use("/assets", express.static(path.join(__dirname + "/assets")));
app.use("/scripts", express.static(path.join(__dirname + "/scripts")));

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/views/index.html");
});

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});
