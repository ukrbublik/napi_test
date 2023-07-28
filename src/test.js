var addon = require('bindings')('napi_test.node')

console.log('This should be eight:', addon.add(3, 5))
