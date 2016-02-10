#!/usr/bin/env node

var fs = require("fs"),
    d3 = require("d3");

// Parse lines.
var lines = fs.readFileSync(process.argv[2], "utf8").split(/[\r\n]+/);

// Parse fixed-width columns.
var data = lines.filter(function(d, i) {
  return i >= 3 && i <= lines.length - 4;
}).map(function(line) {
  var fields = line.split(/\s{2,}/), i = -1;
  return {
    "LAUS Code": fields[++i],
    "State FIPS Code": fields[++i],
    "Area FIPS Code": fields[++i],
    "Area": fields[++i],
    "Year": fields[++i],
    "Month": fields[++i],
    "Civilian Labor Force": +fields[++i].replace(/,/g, ""),
    "Employment": +fields[++i].replace(/,/g, ""),
    "Unemployment": +fields[++i].replace(/,/g, ""),
    "Unemployment Rate": +fields[++i]
  };
});

// Extract the available dates.
var dates = d3.set(data.map(function(d) { return d["Year"] + "-" + d["Month"]; })).values().sort();

// Nest unemployment rate by area and date.
var rateByNameAndDate = d3.nest()
    .key(function(d) { return d["Area"]; })
    .key(function(d) { return d["Year"] + "-" + d["Month"]; })
    .rollup(function(v) { return v[0]["Unemployment Rate"]; }) // leaf nest is unique
    .map(data, d3.map);

// Recast data into a wide table.
var rows = rateByNameAndDate.entries().sort(function(a, b) { return d3.ascending(a.key, b.key); }).map(function(area) {
  return [area.key].concat(dates.map(function(d) {
    return area.value.get(d);
  }));
});

process.stdout.write(d3.tsv.formatRows([["name"].concat(dates)].concat(rows)));
