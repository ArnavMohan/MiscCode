# IMPORT
source('get_team_id.R')
source('team_codes.R')
#Exclude gameID
full_box_score = nbadata[,-1]
#Rename teams according to teamid
team_ids_home = sapply(full_box_score$Home, get_team_id)
team_ids_away = sapply(full_box_score$Away, get_team_id)
#construct dataframe of meaningful statistics
box_score = cbind(full_box_score$Home, team_ids_home, full_box_score$FGM_Home,
            full_box_score$FGA_Home, full_box_score$ASS_Home, full_box_score$BL_Home,
            full_box_score$PF_Home, 
            full_box_score$Away, team_ids_away, full_box_score$FGM_Away, 
            full_box_score$FGA_Away, full_box_score$ASS_Away, full_box_score$BL_Away,
            full_box_score$PF_Away)
box_score = as.data.frame(box_score)

#
# FORMAT FOR box_score:
# V1       team_ids_home V3   V4   V5   V6  V7  V8       
# hometeam homeid        FMGH FGAH ASSH BLH PFH awayteam 
#
# team_ids_away V10   V11  V12  V13 V14
# awayid        FGMA  FGAA ASSA BLA PFA
#

nteams = 1:30
home_ar = rep(NA, 30)
home_br = rep(NA, 30)
home_fr = rep(NA, 30)
away_ar = rep(NA, 30)
away_br = rep(NA, 30)
away_fr = rep(NA, 30)

#
# Construct vectors for each teams assist rate at home and away, block rate at home and away
# Define assist rate = assists/field goals made
# Define block rate = blocks/opponent field goals attempted
# Define foul rate = fouls/minutes played
#

for(i in 1:30){
  #Find games where team i is at home/away
  home_index = which(box_score$team_ids_home == nteams[i])
  away_index = which(box_score$team_ids_away == nteams[i])
  
  #Store each parameter
  hass = box_score$V5[home_index]
  hfgm = box_score$V3[home_index]
  aass = box_score$V12[away_index]
  afgm = box_score$V10[away_index]
  hbl = box_score$V6[home_index]
  afga = box_score$V11[home_index]
  abl = box_score$V13[away_index]
  hfga = box_score$V4[away_index]
  hpf = box_score$V7[home_index]
  apf = box_score$V14[away_index]
  
  #Construct vector from factor
  home_ar[i] = sum(as.numeric(levels(hass)[hass])) / sum(as.numeric(levels(hfgm)[hfgm]))
  away_ar[i] = sum(as.numeric(levels(aass)[aass])) / sum(as.numeric(levels(afgm)[afgm]))
  home_br[i] = sum(as.numeric(levels(hbl)[hbl])) / sum(as.numeric(levels(afga)[afga]))
  away_br[i] = sum(as.numeric(levels(abl)[abl])) / sum(as.numeric(levels(hfga)[hfga]))
  home_fr[i] = sum(as.numeric(levels(hpf)[hpf])) / (48*length(home_index))
  away_fr[i] = sum(as.numeric(levels(apf)[apf])) / (48*length(away_index))
}

#
# Compute league average assist rate / block rate / foul rate
#

#Store each parameter
hass = box_score$V5
hfgm = box_score$V3
aass = box_score$V12
afgm = box_score$V10
hbl = box_score$V6
afga = box_score$V11
abl = box_score$V13
hfga = box_score$V4
hpf = box_score$V7
apf = box_score$V14

#Compute averages
avg_ar = sum(as.numeric(levels(hass)[hass]) + as.numeric(levels(aass)[aass])) / 
  sum(as.numeric(levels(hfgm)[hfgm]) + as.numeric(levels(afgm)[afgm]))
avg_br = sum(as.numeric(levels(hbl)[hbl]) + as.numeric(levels(abl)[abl])) / 
  sum(as.numeric(levels(afga)[afga]) + as.numeric(levels(hfga)[hfga]))
avg_fr = sum(as.numeric(levels(hpf)[hpf]) + as.numeric(levels(apf)[apf])) /
  (48*30*(length(home_index) + length(away_index)))

#Store results in table
ar = cbind(nteams,home_ar,away_ar)
br = cbind(nteams,home_br,away_br)
fr = cbind(nteams,home_fr,away_fr)

#
# Plot results
#

#Plot home assist rate vs away assist rate
plot(home_ar,away_ar,xlab="Home Team Assist Ratio",ylab="Away Team Assist Ratio",
     main="Assist Rate for NBA Teams at Home vs. Away")
#League average
abline(v=avg_ar,col=2,lty=3)
abline(h=avg_ar,col=2,lty=3)
#Regression line
abline(lm(away_ar~home_ar),col=4)
#Null hypothesis: X=Y
abline(a=0,b=1,col=3,lty=4)

#Plot home block rate vs away block rate
plot(home_br,away_br,xlab="Home Team Block Ratio",ylab="Away Team Block Ratio",
     main="Block Rate for NBA Teams at Home vs. Away")
abline(v=avg_br,col=2,lty=3)
abline(h=avg_br,col=2,lty=3)
abline(lm(away_br~home_br),col=5)
abline(a=0,b=1,col=3,lty=4)

#Plot home foul rate vs away foul rate
plot(home_fr,away_fr,xlab="Home Team Foul Ratio",ylab="Away Team Foul Ratio",
     main="Foul Rate for NBA Teams at Home vs. Away")
abline(v=avg_fr,col=2,lty=3)
abline(h=avg_fr,col=2,lty=3)
abline(lm(away_fr~home_fr),col=4)
abline(a=0,b=1,col=3,lty=4)

#
# Perform significance test
# Use paired t test
# H0 = mean(home assist rate) = mean(away assist rate)
# Ha = mean(home assist rate) > mean(away assist rate)
#

#Difference between home assist rate and away assist rate
diff_ar = home_ar - away_ar
#Histogram to check normality
hist(diff_ar,xlab="Home Assist Rate - Away Assist Rate", ylab="Number of Teams")
#Difference between home block rate and away block rate
diff_br = home_br - away_br
#Histogram to check normality
hist(diff_br,xlab="Home Block Rate - Away Block Rate", ylab="Number of Teams")
#Difference between home foul rate and away foul rate
diff_fr = away_fr - home_fr
#Histogram to check normality
hist(diff_fr,xlab="Away Foul Rate - Home Foul Rate", ylab="Number of Teams")
#Perform paired t tests
ttest_ar = t.test(home_ar,away_ar,paired=T, alternative="greater", conf.level = 0.9)
ttest_br = t.test(home_br,away_br,paired=T, alternative="greater", conf.level = 0.9)
ttest_fr = t.test(away_fr,home_fr,paired=T, alternative="greater", conf.level = 0.9)

#
#
#
#
#

