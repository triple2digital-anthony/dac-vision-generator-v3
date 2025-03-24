const redCodes = `7yazynvr3et5696c865gxxkv9a
7defr7yuawd7z2wsnt54qk2jqw
7kfdqnhwvfgrnz82hwbyv38x66
7v5mbf4575hgyx943dxt6p3wd6
72hmpymwerga943mmpbt8jqfha
7pbauud87gszsnyixw9xbztrfn
646an4wujcsfpq5iacczs76zue
vtetvitey56reyvzevzxicts82
7hnssk98kewrzah2imcd2gecqa
v8px5pyzhtjhcby3vv3aseqdxs
7yah9tgc2wii27c8w6x7qmrx5e
vxpix6d933jhpt38ghq8svru72
77hvgnu3evdqrf4rkc8mreh3ua
73993i2xyhtjg5v99jd7ijedws
7par52rph9fyeq9zvg94h9aene
vwzsnbvvp6xf6vgiv88vji698s
7z3898hqhfy8q9bc44zdzfmmk2
7hraucy3k2ke827ky6itwf9pg2
vwxiw4ht9ncp9ffhe6ekbaj97n
v8nswzt4zdvmkgjk3kjysd7wuw
7c6s4bps3c3usv2mjj9twr7eye
649p8f2pzkzp56835tvvxucmsw
vjiwc546sqtddwygx65skk7wa6
vn8qwpzrwbm4dbpc5843a57ue2
7v895yjshzm34wn7yd88hwdb8a
visc7sgvx2pyfx4ya5qb7s2g8e
vphpiu7bn3wm95kiwkfp9aprye
v8pxrsnrnhne9w5crfwthqpd8n
7hnz29pepypsy67x9z6hf9if7w
v8nzkgsh3iqssj4w32jpmqsriw`;

const codes = redCodes.split('\n');
const prefixes = {};
const firstChars = {};

// Count prefixes (first 3 characters)
codes.forEach(code => {
  const prefix = code.substring(0, 3);
  prefixes[prefix] = (prefixes[prefix] || 0) + 1;
  
  const firstChar = code.charAt(0);
  firstChars[firstChar] = (firstChars[firstChar] || 0) + 1;
});

// Sort prefixes by frequency
const sortedPrefixes = Object.entries(prefixes)
  .sort((a, b) => b[1] - a[1])
  .map(([prefix, count]) => `${prefix}: ${count} (${(count / codes.length * 100).toFixed(1)}%)`);

// Calculate first character distribution
const totalCodes = codes.length;
const firstCharDist = Object.entries(firstChars)
  .sort((a, b) => b[1] - a[1])
  .map(([char, count]) => `${char}: ${count} (${(count / totalCodes * 100).toFixed(1)}%)`);

console.log('Red Cap Codes Analysis:');
console.log('Total codes analyzed:', codes.length);
console.log('\nFirst character distribution:');
console.log(firstCharDist.join('\n'));
console.log('\nCommon prefixes (first 3 characters):');
console.log(sortedPrefixes.join('\n'));

// Extract all unique prefixes
console.log('\nAll unique prefixes:');
console.log(Object.keys(prefixes).sort().join('", "')); 