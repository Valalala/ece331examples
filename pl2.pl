#!/usr/bin/perl
my @x=`ps augx`;
#print "@x\n";
foreach (@x) {
	#  default index var
	next if (/^USER/);
	@y=split(' ');
	#$process[$y[1]]=\@y;
	#$tmem+=$y[4];
	#print "\n";
	$process[$y[1]]=[@y];
}
#print "$tmem\n";
#print "@process";
#print "$process[52]";
#print @{$_} . "\n";

foreach (@process) {
	next unless (@{$_});
	#print @{$_};
	#print "\n";
}

print $process[52]->[10];
print "\n";

