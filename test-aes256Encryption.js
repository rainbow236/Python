var aes256Cryto = require("./aes256Encryption");

// for test
var str = '123456';
var key = 'NeGqWKgwp07QXPdnh0HsEgkpEeb25SamoBU3bFRh1IQ=';
var iv = 'RH/nP5lzsAC7+LRidCmsGw==';

afterEncrypted = aes256Cryto.Encrypt(str, key, iv);
console.log('encrypt->',afterEncrypted);

afterDecrypted = aes256Cryto.Decrypt(afterEncrypted, key, iv);
console.log('decrypt->',afterDecrypted);