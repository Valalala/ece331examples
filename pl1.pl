#!/usr/bin/perl
$\="\n";
$,="\n";
#print 1 .. 10;
@x=(1 .. 10);
#print @x;
#print $#x . "\n";
#$x[100]=43;
#print @x;

&def(\@x);
&def(\@y);

print "skdjf @{[def($e)]} jkhdfs";

sub def {
# @_ are the args
	print @_;
	if (@{$_[0]}) {
		print "Defined";
	} else {
		print "undefined\n";
	}
}

