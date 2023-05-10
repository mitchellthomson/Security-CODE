const crypto = require ('crypto');
const secret ='cFDj9XpH3EgmZb5RyqLxhnvKuVtWo6wa' 
const encrypt = () => (password) =>{
    const iv = Buffer.from(crypto.randomBytes(16));
    const cipher = crypto.createCipheriv(
        'aes-256-ctr',Buffer.from(secret),iv);

    const encryptPass = Buffer.concat([cipher.update(password),cipher.final()]);

    return {iv:iv.toString('hex'), password: encryptPass.toString('hex')};
};

const decrypt = () => (encryptPass) => {
    const decipher = crypto.createDecipheriv('aes-256-ctr',Buffer.from(secret),
    Buffer.from(encryptPass.iv, "hex")
    );

    const decryptedPass = Buffer.concat([decipher.update(Buffer.from(encryptPass.password, "hex")),decipher.final()]);

    return decryptedPass.toString();
};

module.exports = {encrypt, decrypt};