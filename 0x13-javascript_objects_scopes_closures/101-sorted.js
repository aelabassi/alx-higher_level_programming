#!/usr/bin/node
const dict = require('./101-data').dict;
const listKV = Object.entries(dict);
const values = Object.values(dict);
const uniqueValues = [...new Set(values)];
const sortedDict = {};
for (const value of uniqueValues) {
  sortedDict[value] = listKV.filter((kv) => kv[1] === value).map((kv) => kv[0]);
}
console.log(sortedDict);
