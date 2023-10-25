const promise = new Promise((resolve, reject) => {
  if (true) {
    resolve("Shob thik ase");
  } else {
    reject("sobi valo");
  }
});

promise.then((res) => res + " kintu ami thik nai")
  .then((res2) => console.log(res2))
  .catch((err) => console.log(err));
