/**
 * Generates a number starting with 07, the third digit is between 3-9 and the
 * remaining 8 random digits have no restrictions.
 */

function generateMobileNumber() {
  const random = Math.random();
  return `07${Math.floor((random * 7) + 3)}${String(random).slice(2, 10)}`;
}

generateMobileNumber();
