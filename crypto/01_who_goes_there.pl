=for comment

    the system asks for your username.

    But no. =/ That's not the correct answer. 
    
    But in the automated reply there is the hint: 
    it asks for the reverted name instead. 

    PERL would do the job . . 

=cut

print "Please input your username\n";

$uname = <>;
chomp($uname);

print "your answer: ", scalar reverse( $uname ), "\n";
