const testAddon = require('./build/Release/node_soundio.node')
console.log('addon', testAddon)

testAddon.test();

module.exports = testAddon