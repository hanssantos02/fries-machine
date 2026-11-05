# Prototype build — work with received materials

> **Current save, 6 November 2026:** [Concise assembly checkpoint](ASSEMBLY_CHECKPOINT.md) and the newest dated reports supersede earlier pending prompts below. **Step37 motor soldering has been issued but is not reported complete.** Firmware remains output-free simulation; no powered motor test or Phase3.

## Current Step37 — MOTOR+ and banded diode lead to motor terminal A

**Steps35/36 result, 6 November2026:** user confirms working as intended/secured in response to beep/beep/no-beep and DRIVER+retention question. Record continuity of both positive branches, isolation from connector− and DRIVER+clamping by user report. No numeric resistance, photo or rated-current test supplied. Preserve taped junction and negative return; don't repeat completed tests without a reason.

The SR5100 is the flyback rectifier. In the intended one-direction low-side circuit, its **banded cathode connects to motor positive**; its unbanded anode will later connect to the motor's switched return/LOAD side. The band is a direction mark, not a universal instruction to connect to supply negative. Reversing this diode can make a short across the supply when the driver turns on. Attach only its positive side at this checkpoint and keep power off.

### Terminal identification

Photo09 shows two bare rear motor contacts, but no reliable factory polarity marking. If an actual+mark is now visible, use that contact asA and show it if uncertain. Otherwise choose one contact and label it **A / bench positive**, leaving the other **B / future LOAD**. This is a chosen bench polarity, not a claim about factory markings or clockwise rotation. No motor direction/load test yet. Do not reverse the adapter later to change direction; both motor lead assignment and diode orientation would need coherent review.

| Part | Connect to | Purpose |
|---|---|---|
| Lead labelledMOTOR+ from fused junction | Motor terminalA | Future fused positive feed to motor |
| SR5100 lead at white/silver-banded end | Same motor terminalA | Cathode at positive node for turn-off protection |
| Unbanded diode lead | Leave free/isolated this step | Future anode connection atB/LOAD |
| Motor terminalB | Leave empty | Return lead follows at next checkpoint |

### First motor solder joint only

**Before soldering:** unplug USB, adapter wall and output; fuse remains removed. LOAD/control terminals empty. Secure motor on a heat-resistant nonconductive support without crushing its casing, gearbox or rear plastic. Keep shaft clear; do not hold the hot joint with fingers. Use a stable iron stand, eye protection and ventilation/fume extraction, avoid fumes and use electronics solder/flux only. Hot copper/iron can burn; prolonged heat can loosen the contact in the plastic end cap. Wash hands after solder handling.

1. IdentifyMOTOR+tail by its label (black insulation does not mean negative) and terminalA as above. Adjust stripped length only enough to make a tidy attachment to the actual contact; don't cut strands or leave excessive bare conductor. If contact is inaccessible or damaged, stop and report rather than force it.
2. Position the diode near the motor's rear with its body/leads clear of the metal case, ventilation openings, shaft and moving parts. Shape only the leads, supporting them with pliers rather than levering against the diode body. Leave enough lead/slack to reach both contacts later without tension. Do not cut a lead too short to reach/support the futureBconnection.
3. If heat-shrink sleeves will be used, pre-position them on relevant leads away from the hot joint before soldering. Do not cover the joint yet; properly applied electrical insulation tape may instead be used after inspection for this dry bench setup. Planned insulation must cover the exposed contact and diode leg without interfering with the shaft/vents.
4. Bring theMOTOR+wire and the diode's **banded-end lead** together at terminalA. Form a light retaining bend/hook around the actual contact if its geometry allows, without bending or twisting the motor contact itself. Support the diode/wire weight in a holder. Do not wrap bulky conductors with force or solder a loose plastic jumper socket to the pin. If they cannot be positioned securely, send a photo before improvising.
5. With a clean lightly tinned iron tip, heat contact/conductors and add electronics solder until it wets all intended metal. Use only enough solder/heat to make the joint; no large blob or long cooking of plastic. If solder does not flow promptly, remove heat, let it cool and investigate tool/flux/contact cleanliness. Stop for moving pin, softened plastic or damaged insulation. Keep solder clear of terminalB and the motor case.
6. Let the joint cool naturally without movement. Inspect banded lead atA, solder bonded to contact/wire/diode lead, no stray strands/bridge/case contact and no damaged plastic. Gently test lead retention while supporting the motor contact, without levering/bending it. Keep the other diode lead disconnected, isolated fromA/case, and the motor'sBterminal empty.

**Check before continuing:** request a close photo showing the cooledAjoint, band position and both motor contacts, plus whether the wire/diode lead stay attached under a gentle check. Stop before covering, makingBjoint, inserting fuse or connecting power/control. One-ended diode attachment is not a completed flyback circuit. Return lead/diode anode, joint insulation/strain relief, module topology/ratings, safeOFF and secured unloaded motor/disconnect remain later checkpoints.

Reference: [Adafruit motor flyback-diode orientation example](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors?view=all). Its band-to-positive principle applies; its5V/breadboard/transistor wiring and motor ratings are not this12Vproject's wiring or ratings.

## Current Step36 — reconnect DRIVER+ after junction insulation

**Latest report, 6 November2026:** user says junction done and already covered with electrical tape. Record tape in place, no new photo. Don't automatically unwrap it just to return to the earlier inspection stage. The three Step35 results were not individually stated; ask whether they were beep/beep/no-beep alongside this connection's completion report. Do not record a measured pass or energize on ambiguous “done.” Further unpowered wiring can proceed independently of that clarification.

Electrical insulation tape is acceptable for this dry low-voltage bench junction if it fully encloses all bare joint metal, overlaps intact insulation and stays secure. Check coverage from all sides, especially the gap between the two outgoing wires. No exposed strand, lifted flap or sharp point may protrude. The cooled solder joint must already be mechanically firm; tape cannot make a loose joint sound. Provide support/slack so cable movement does not pull on the splice. This does not qualify final fryer-area heat/moisture resistance. If insulation is incomplete/uncertain, stop and show the issue rather than applying power. Heat-shrink was planned, not mandatory regardless of the actual insulation outcome.

1. Keep USB/adapter unplugged, adapter plug out of the connector and fuse removed. Motor, SR5100, LOAD/control wiring remain disconnected. Leave negative-return wire intact.
2. Identify the outgoing lead labelledDRIVER+, distinguishing it from the other positive lead labelledMOTOR+. Black insulation does not make these negative wires. Use labels and the intended node map; if lead identity is lost, resolve it before connecting.
3. Fit onlyDRIVER+into the modulePOWER+terminal on the three-way+, LOAD,−block. Use existing short untinned stripped end, adjusting to actual clamp depth if needed. Clamp copper, not insulation, with no stray/excess exposed conductor and one wire per terminal. Do not force a poor fit, remove strands or solder-tin the screw-clamped end.
4. Tighten without stripping the screw and gently pull the insulated lead while supporting the connector. Keep the unusedMOTOR+tip individually insulated and disconnected. Do not attach motor or insert fuse.

**Check before continuing:** ask whetherDRIVER+is secured and whether previous junction results were beep (junction→DRIVER+), beep (junction→MOTOR+), no beep (junction→connector−). If earlier tests were not performed or displays differed, record that and prepare a targeted accessible test without unnecessarily stripping the taped splice. No repeated tests needed if user clearly confirms expected results. This step does not authorize power, control wiring, flash or motor attachment.

## Current Step35 — check the soldered positive junction before insulating

**Step34 result, 6 November2026:** user reports junction “done, and secured.” Accept assembly/gentle-retention by report; no close photo or measured electrical result supplied. Do not claim independent solder inspection or repeat the soldering procedure. Driver+was released for preparation; both branch far ends are still disconnected, negative return retained, fuse out. No power is permitted.

1. Keep adapter unplugged from wall AND connector, USB unplugged, fuse removed, motor/diode/control disconnected. Keep both DRIVER+/MOTOR+ far ends disconnected and driverPOWER+empty so the junction is isolated from module electronics. Leave sleeve back for access to the cooled solder joint.
2. Inspect for loose copper strands, sharp spikes, damaged/melted insulation or a conductor moving in the joint. If any defect is present, stop and show it; do not hide it under tubing. If tubing was already shrunk, report that before removing/cutting anything; adapt the test access instead of automatically undoing insulation.
3. Strip only about4mm from each labelled branch far end to expose probe contact. Keep all strands and keep ends away from each other/the negative assembly. Actual clamp/motor attachment strip lengths can be adjusted at their later steps. Do not solder-tin the future DRIVER+ screw-clamped end.
4. Meter blackleadCOM/redleadVΩ, not current jack; select continuity/beeper mode. Touch tips together to establish beep/lowresistance and separate them to establish open. If the baseline fails, correct meter mode/lead contact before judging the joint.
5. Touch one probe to the bare solder junction where the red stem joins the pigtails, the other to the labelledDRIVER+ far end. Expected beep/lowresistance near the probe baseline. Swap colours if easier; this is a passive conductor path. Record result.
6. Keep the first probe at the same red-stem junction; test the labelledMOTOR+ far end. Expected beep/lowresistance. Record result.
7. Test that junction against the DC connector terminal marked− (or verified driverPOWER−). Expected no beep/open. This checks for accidental connection of positive junction/loose strands to the negative return, with driver+and motor still disconnected. Prevent probe/loose-wire contact from creating a false short.

**Check before continuing:** request the three results in order (DRIVER+, MOTOR+, negative isolation). Stop before heat shrinking, connecting a branch, inserting fuse or power. Passing continuity cannot qualify current capacity/thermal performance, fuse coordination or the full circuit. After the report, inspect/insulate/support the junction and reconnect the DRIVER+tail as a single conductor at its own checkpoint.

## Current Step 34 — solder the fused-positive Y junction

5 November2026. User confirms no3port junction connector and chooses existing wire, solder and heat-shrink. This replaces the direct fuse-output→driver+ segment with one input and two outgoing leads, keeping one conductor under the driver's screw. No new purchase is needed for this selected method. No junction assembly is reported complete yet.

### Planned connections — all one positive electrical node

| Lead | Destination | Material / identification | Why |
|---|---|---|---|
| Incoming stem | Existing red output tail of first fuse holder | Existing holder wire; fuse remains upstream and removed | Brings the protected branch supply to the split |
| Branch1 | Future driverPOWER+ connection | Short18AWGstranded-copper pigtail, labelDRIVER+ / POS+ | One conductor fits the driver's+clamp |
| Branch2 | Future selected motor positive connection | Short18AWGstranded-copper pigtail, labelMOTOR+ / POS+ | Supplies motor positive from the same fused branch |

```text
connector+ -- holder[FUSE OUT] -- red output -- soldered junction -- DRIVER+ tail
                                                               └-- MOTOR+ tail
The two tail FAR ENDS remain insulated and disconnected for inspection.
Driver+ is temporarily empty; driver− return remains connected as before.
```

### Prepare only this junction, then stop for inspection

**Before work:** unplug USB and adapter from wall/connector; remove fuse. Leave motor and diode disconnected. Clear metal offcuts from the work surface. Use a stable iron stand and heat-resistant surface, eye protection, ventilation/fume extraction, and avoid breathing solder fumes. Secure wires in a holder away from fingers/plastic, without crushing insulation. Use electronics solder/rosin or electronics no-clean flux, never plumbing acid flux. Keep hot tip/barrel away from skin, insulation and the fuse-holder plastic; wash hands after handling solder, especially leaded solder.

1. Loosen driverPOWER+ and release only the red fuse-holder output lead. Leave the DCconnector+ feed and black negative-return connections intact. The released red tail is the incoming stem. Do not cut the existing negative return or alter input/LCD wiring.
2. Cut two short18AWGstranded-copper wire pieces that reach the driver and intended nearby motor with slack (for example around10–15cm for the nearby driver,20–30cm for the nearby motor; adjust to actual layout rather than pull wires taut). They are positive leads even if insulation is black: label both ends POS+ and destinations DRIVER+/MOTOR+. Leave their far ends unstripped and disconnected. If existing wire/insulation is unsuitable or reach needs much longer leads, report before substituting a thin jumper or assuming ratings.
3. Strip roughly8mm from one end of each pigtail and from the freed red stem, adjusting to make a compact mechanically engaged joint without nicking strands. The previous screw-terminal stripped length may need slightly more insulation removed. Keep all strands; do not remove strands to reduce bulk. Do not strip the pigtail far ends yet.
4. Before joining, slide an adequately sized heat-shrink sleeve onto the loose red stem and park it well away from the soldering area. It must later pass over the whole joint and overlap intact insulation on both sides (single stem and paired branches), shrink to a snug insulated covering and leave no copper exposed. A sleeve around25–30mm long can suit a compact roughly8mm joint, but actual bundle diameter/shrink ratio determine fit; this is not a fixed required tube size. If available tubing cannot cover/grip the arrangement, stop and show the tubing rather than assemble an uninsulatable joint. Do not slit tubing to force it over the connection.
5. Align the two pigtails side by side with stripped ends pointing together; twist their exposed copper into one neat pair. Form that pair and the red stem into opposing hooks, link them and wrap the free copper around the mating bundle so they remain mechanically engaged without being held by molten solder. The red stem extends one way and the insulated pigtails extend the other, allowing the sleeve to slide across the finished joint. Keep it compact and smooth, with no spikes/broken strands. Do not make a same-direction three-wire end-cap that leaves an open exposed tip or hold three loose ends together using only a solder blob. A light pre-solder check should not separate the joint.
6. Secure the joint; clean/lightly tin the iron tip. Heat the copper junction, then feed electronics solder onto the heated copper until it wets all three conductors. Use enough to bond/fill the joint without a large ball. Do not drip solder onto a cold bundle or let solder wick far under insulation to make long stiff leads. If solder will not wet, stop, cool and check tool/flux/cleanliness; don't keep cooking insulation. Hold still while solder sets and allow natural cooling before touching it.
7. Once cool, inspect for bonded conductors, no loose strands or melted insulation, and gently pull each of the three insulated leads while supporting the joint. No wire should move or separate. Matte lead-free solder is not automatically a fault; surface shine alone does not prove a sound bond. Keep sleeve parked back so the bare joint is visible in a close photo. Keep both pigtail far ends insulated/disconnected, driver+empty, fuse out and all power unplugged.

**Check before continuing:** ask for a close photo of the cooled, uncovered junction and whether all three leads stay secure under a gentle pull. Stop before shrinking the sleeve, reconnecting driver+, motor attachment or power. Next check/insulate the joint, verify electrical paths and add strain relief before completing connections. Electrical tape/heat-shrink do not replace a sound metal joint; solder must not be added to future screw-clamped ends. This bench-splice step does not qualify the entire supply/protection, motor mechanics or safeOFF logic.

Reference: [Adafruit3way wire-splice method](https://learn.adafruit.com/make-it-glow-how-to-solder-neopixels-a-beginners-guide/splicing-wires). Project lead lengths, labels, inspection staging and protection scope above are our build choices, not manufacturer requirements for this generic module.

## Current Step 33 — inspect motor terminals and plan fused-positive junction

### Photos received — choose the positive junction method next

Photos09–11 in [evidence manifest](assets/motor-review-2026-11-05/manifest.json) now show the requested parts. Motor rear has two bare electrical contacts; no dependable+ /− marking is readable in this angle. Connector red/black and driver's outer red/black power leads are consistent with intended map; centreLOAD/control block remain empty. A fuse is pictured separately. No new measured mapping, terminal clamp rating or rated-load result is inferred. The earlier photo request below is satisfied.

Next establish whether the user owns a small3port connector whose entries are electrically common (for example, a suitable lever wire connector). A multi-position terminal strip may have isolated pairs, so inspect the actual part instead of assuming it joins all entries. If present, request a photo/model and verify compatibility with all conductors. If absent, a properly prepared soldered insulated junction using existing wire/heat-shrink is an alternative; do not impose a new purchase solely to branch one bench channel. An availability question is pending; no junction method has been selected/performed.

Intended node, conceptual only:

```text
Fuse-holder output ---- positive junction ---- short lead to driverPOWER+
                                        └---- lead to future motor positive
```

This junction replaces the current direct fuse-output→driver+ segment when the method is chosen. Each module screw should retain one suitable conductor unless documented otherwise; do not stuff another lead into its occupied+terminal. The fuse remains upstream of both branches. Keep motor disconnected and no terminal polarity assignment yet. Clear the visible metal offcuts from the work area before later electrical testing. Keep adapter/USB unplugged and fuse removed while handling; no motor power, control wiring or flash is issued here.

**Step32 result, 5 November 2026:** user reports both negative-return ends secured and confirms using18AWG. Accept DCconnector−→driverPOWER− as connected/retained by user report; no new photo or electrical load/current-rating test. The20AWG alternative was discussed but is not recorded installed. Keep completed power leads and input/LCD wiring intact.

Before attaching motor leads and the flyback diode, inspect the actual motor contacts and existing terminal layout. On the intended low-side driver arrangement, the fused-positive node must serve both the driver+ and motor positive; the motor's other side goes to LOAD, not straight to supply−. A photo of a terminal cannot certify that it accepts multiple conductors: choose a documented suitable junction/termination or properly prepared insulated pigtail method later, rather than assuming two wires can share a screw. No hookup is issued from this conceptual description; actual module topology/ratings are still to resolve before powered use.

1. Keep USB and adapter unplugged, adapter output out of the connector and fuse removed. Motor, diode and control terminals remain disconnected.
2. Request a close photo of the selected motor's rear/electrical end showing both contact lugs or existing leads, any+ /−markings and surrounding plastic. The previous motor-front label photo establishes12V22RPM, not terminal attachment details.
3. Request a clear photo of the currently assembled DCconnector, fuseholder and driver, with wires/terminal labels/entry points visible. Do not dismantle successful connections solely for the photo. If underside labels are needed, support the unpowered module without straining its wires.

**Check before continuing:** wait for photos. Use them to choose motor/diode attachment and the secure fused-positive split; do not tell the user to push a second conductor into an undocumented occupied terminal. Review for obvious stray strands/insulation clamping, keeping visual review distinct from measured current/thermal acceptance. No repeat store voltage/connector continuity/diode test without a specific new cause. No fuse replacement, power, flash or new GPIO yet.

## Current Step 32 — DC connector negative to driver power negative

**Wire choice clarification:**18AWG is a conservative recommendation using owned stock, not a unique requirement for this single-motor bench return. Genuine20AWGstranded copper is an acceptable alternative for a short isolated one-channel lead, with intact insulation, secure clamp fit and cool/unbundled bench routing. Aim10–30cm rather than a long loose extension; this is a chosen bench scope, not a universal current-rating cutoff. The proposed2Abranch fuse and actual wire/holder/connector matching still require completion/qualification before power; seller1.2Astall is not measured. No thin DuPont/breadboard path. Do not reuse this permission for a shared three-motor supply/return, full5Atrunk or basket/mains/final harness without reviewing combined current, route, temperature and protection. No automatic change to B04 final allowance or purchase. Source: [PowerStream wire resistance/current-sizing guide](https://www.powerstream.com/Wire_Size.htm), which treats ampacity tables as guidelines dependent on installation, insulation and heat. No universal ampacity assigned to the user's unidentified wire.

**Step31 result, 5 November 2026:** user reports remaining holder tail secured in driverPOWER+. Accept wiring/retention by report; no photo/current-rating inspection supplied. Preserve that connection and the successful USB logic wiring.

Motor current needs a proper return to the supply. Use the module's POWER− terminal on the three-way+, LOAD,− block; controlGND besidePWM is the signal return and is not a substitute for motor-power wiring. This step completes only the unpowered supply pair, not the motor or control circuit.

1. Keep USB unplugged, adapter unplugged from wall AND DC connector, and fuse removed from holder. No motor/diode/control wires connect to this assembly yet.
2. Take owned18AWG black stranded power wire, or the short20AWGstranded-copper alternative within the scope described above. Cut a length that comfortably reaches from connector− to driverPOWER− with slack; route away from other bare terminals, avoiding tension. Do not use a thin DuPont jumper or breadboard rail for this current path. If colour is not black, label both ends as this branch's negative power return.
3. Strip only enough at each end for actual terminal depth (about4–5mm initially). Do not nick/remove strands. Twist strands together; if conductor cannot fit/clamp securely, stop and report. Do not force wire or solder-tin it as a screw-terminal workaround.
4. Clamp one end in the DC connector terminal marked−. Clamp the other in the driver's POWER− on its three-way block. Use actual printed labels; do not use LOAD or the separate controlGND. One conductor per screw at this stage, clamped on copper, not insulation.
5. Inspect for no loose strands/excess bare copper near+, LOAD or PCB metal. Gently tug each insulated end while supporting its connector to check retention; do not strip screws by overtightening.
6. Leave fuse removed and all supplies disconnected. DriverLOAD/controlPWM/controlGND stay empty; no motor, diode or Mega wiring attaches to this power assembly.

**Check before continuing:** ask whether connector−→driverPOWER− is secure at both ends, with fuse out/adapter disconnected. If a terminal label or fit is uncertain, request a close photo before further handling. This is not permission to fit the fuse or energize; actual connector/holder/wire/fuse matching, topology, motor-positive junction, flyback, safeOFF and secure unloaded mounting/disconnect remain pending.

## Current Step 31 — remaining fuse-holder lead to driver positive

**Step30 result, 5 November 2026:** user reports “done and secured” after loop preparation, first holder lead→DCconnector+ and retention instructions. Accept physical completion by report; no new photo or rated-current check supplied. Do not repeat the same connection. Keep the fuse OUT and adapter disconnected from connector/wall.

1. Unplug MegaUSB and every supply. No motor or control wiring may attach to the loose driver. Keep LCD/input wiring intact but unpowered.
2. Select one previously identified module. On its three-way POWER terminal block use the actual printed **+** label. In the saved underside photo20, the three terminals are+, LOAD,− from top to bottom in that view; rotation changes apparent position. Do not use the separate PWM/GND control terminals, and do not infer the terminal from screw colour alone. If+ cannot be identified, request a clear underside photo before wiring.
3. Take the remaining free holder tail. Remove any temporary end insulation; strip only enough wire to fit the terminal clamp (approximately4–5mm initially, adjusted to actual clamp depth), with no nicked or loose strands. Twist strands gently together; insert into the wire-entry opening for+, not around the screw head. If it cannot fit or clamp securely, stop and report; don't force, remove conductor strands or add solder to fake a pin.
4. Tighten without stripping the screw. Gently pull the insulated lead to check retention. The clamp must grip conductor, not insulation, with no exposed strands reaching LOAD/− or nearby PCB metal.
5. Leave moduleLOAD/−/PWM/GND and connector− empty. No motor, diode, Mega or breadboard connection is made to this assembly yet. Fuse stays removed; adapter plug stays out. Support the module on a dry nonconductive surface; no power is applied.

**Check before continuing:** ask whether remaining holder tail→driver+ is secure with fuse out and adapter disconnected; request photo if terminal identification/retention is uncertain. A secure joint is not complete channel acceptance or permission to insert fuse/power. Driver topology, adequate fused-positive motor junction (do not assume terminal accepts two wires), negative power return, protection/ratings, safeOFF and secured motor/disconnect remain later checkpoints.

## Current Step 30 — first fuse-holder lead to connector positive, unpowered

### Latest: user confirms the cable is still one loop

The loop must become two separate tails to insert the holder in series with the positive supply. This is one cut through the red insulated cable, not a cut into the plastic holder. The earlier instruction below to stop and report loop status has now been satisfied. No cut is reported completed yet.

1. Confirm USB and adapter unplugged, adapter plug OUT of connector, holder completely disconnected and fuse removed. Do not cut any cable attached to an energized supply or existing circuit.
2. Find approximately halfway along the red wire between the two places where it enters the holder. This is normally the far side of the loop from the holder body. Keep the two resulting tails roughly equal for useful lead length; do not cut near the holder where a tail would become too short.
3. Use wire cutters to make ONE cut at that midpoint, leaving two separate free tails. Keep fingers out of cutting jaws and wear eye protection. Do not cut any other cable or the holder body.
4. Strip just one free tail to suit the connector clamp (about4–5mm initially, adjusted to actual terminal depth). Avoid nicking strands, twist them together and clamp that end in the DC connector terminal marked+. No exposed strands toward− and no clamp on insulation. Do not force an oversized conductor or tin it with solder as a screw-terminal workaround.
5. Check gentle-pull retention. Leave the other tail insulated: its fresh cut end should not expose protruding strands; cap/tape it separately if necessary. Do not strip the second tail yet. Connector− remains empty and fuse stays OUT. Adapter, motor, module and Mega remain disconnected from this assembly.

**Check before continuing:** request clear photo of the prepared holder/+connection and confirmation it stays attached under a gentle pull. No power/fuse replacement or more wiring until reviewed. The holder's actual lead gauge, ratings and whole-channel protection remain unresolved by making this connection.

**Step29 result, 5 November 2026:** user reports all three connector mapping checks working as intended (+centre/−outer continuity, +to− isolated). Record qualitative PASS by report, not measured contact current capacity or a live adapter test.

The branch fuse goes in series with positive supply: motor-branch current must pass through it before reaching the driver/motor circuit. Either lead of a normal passive fuse holder can face the supply; it has no polarity. This checkpoint only makes one unpowered connection, not a complete protected circuit.

1. Unplug Mega USB and adapter from the wall. Keep adapter plug OUT of the DC connector. No motor, module or electronics attach to this loose assembly.
2. Open the fuse-holder cap and REMOVE the fuse; leave it out.
3. Check whether its red cable has two separate free ends. Photo02 appears to show an uncut loop: if still a continuous loop, stop and report that before cutting. No cutting is instructed by this step. If there are already two free ends, use either one below.
4. Loosen the DC connector screw marked+. Strip only the insulation length needed to enter the terminal clamp (about4–5mm as an initial guide, adjusted to actual terminal). Do not nick/remove strands. Twist strands gently together; insert conductor fully into the wire-entry hole, not around the screw head. Ensure the clamp grips copper, not insulation, with no stray strand reaching−. Do not force oversized wire or tin strands with solder as a screw-termination workaround. Stop if wire cannot fit/clamp securely.
5. Tighten securely without stripping the screw. Hold the connector and gently pull the insulated lead: it should stay retained. No torque/current rating is inferred. Individually insulate any bare free holder end with a suitable cap/electrical insulation tape; an open heat-shrink tube alone does not seal a tip. Keep connector− empty.
6. Leave fuse out and all supplies disconnected. Do not attach the driver, motor or Mega yet.

**Check before continuing:** ask for a clear photo of this+connection and gentle-pull result, OR confirmation the cable is still a loop. Wait before further wiring/fuse replacement. No energized test is issued; remaining wire/holder/connector/fuse matching, full topology, safeOFF/reset and secured motor/disconnect remain pending. Earlier connector-mapping prompts below are superseded by the reported pass.

## Current Step 29 — check the disconnected DC connector's terminal mapping

**Step28 result, 5 November 2026:** user confirms SR5100 and reports a forward result with redunbanded/blackbanded, none reversed. That is consistent with expected directional behavior if reverse displays OL/open; numeric0.000 is different and needs review. Exact displays/meter mode not supplied, so do not invent values or claim a rated-current test. Do not repeat the same test without a new reason. Band is cathode; opposite end is anode, not permanent positive/negative supply labels for every circuit.

The barrel-to-screw connector converts the adapter plug into two wiring terminals. Its moulded plus/minus marks must be mapped to the actual centre/outer contacts before wiring a centre-positive supply; this check uses only the loose passive connector, not a powered adapter.

1. Unplug USB and the adapter from the wall. Remove the adapter plug and every wire from the screw connector. Test only the completely disconnected connector. Never use continuity mode on an energized supply or outlet.
2. Keep black meter lead inCOM and red inV/Ω, not a current jack. Select continuity/beeper mode. Briefly touch the probe tips together to establish beep/low resistance and separate them to establish open; if this does not work, clarify meter mode before continuing.
3. Touch one probe to the metal of the screw terminal marked+, the other to the barrel's centre contact. Expected beep/low resistance near the shorted-probe baseline. Colours may be exchanged for these passive metal-contact checks.
4. Test marked− terminal to the outer barrel contact. Expected beep/low resistance. Touch the contact itself, not black plastic, and do not bridge centre and outer with one tip.
5. Test+ terminal against− terminal, with probes kept apart. Expected no beep/open; this checks for an unintended connection between the two isolated paths. A real short, unexpected mapping or unstable contact must be resolved before power.
6. If the centre contact is inaccessible or unclear, do not force the probe or push anything inside. Send an end-on photo of the barrel opening so contacts can be identified. Leave the connector disconnected after the check.

**Check before continuing:** ask for three results: +to centre, −to outer and+to−. Wait before wiring. This proves only low-current contact mapping/isolation; it cannot establish a connector's current capacity, correct plug dimensions under load or supply polarity/performance. No new powered adapter measurement or motor test is directed.

## Current Step 28 — isolated flyback-diode check, 5 November 2026

New [diode photo](assets/motor-review-2026-11-05/07-axial-diode.jpg) shows a black axial rectifier-style component with a pale band at the upper-right end in that orientation. This is the intended component style, unlike the red LED. Full body code is not reliably legible; ask the user to transcribe it while testing. Do not assert manufacturer/authenticity or current capacity from appearance. No electrical result yet.

The band identifies the **cathode**; the opposite end is the **anode**. These names define a diode's direction. A digital multimeter's diode mode applies a small test current and displays forward voltage drop; this is different from a motor-power or current-capacity test.

**Before testing:** leave the diode completely disconnected from motor, driver, breadboard and all supplies. Unplug Mega USB and adapter before handling nearby wiring. Never use diode/continuity/resistance mode on a powered circuit. Only probe the loose diode, not an adapter or household outlet.

1. Put the black meter lead in COM and red in the V/Ω/diode jack, never the A/mA/10A current jack. If actual labels differ or the mode is unclear, send a meter photo before guessing.
2. Select diode mode using its diode symbol. On a combined continuity/diode setting, use SELECT/FUNC as appropriate to show diode mode; do not rely on a continuity beep.
3. Hold red on the unbanded lead (anode), black on the banded lead (cathode), touching separate metal leads with probe tips kept apart. Record the displayed number/unit. A conducting diode normally shows a forward-drop number; no exact pass window is imposed without the meter/part context. Schottky drops can be lower than ordinary silicon-diode examples.
4. Swap probes: red on banded, black on unbanded. Record display. Normally this is OL/open at the meter's test conditions. OL is an open/over-range indication here, not measured zero volts.
5. Transcribe the body code, expected selected stock SR5100, and report both readings. Do not wire or solder it into the motor channel yet.

**Check before continuing:** wait for two readings and code. A near-zero result both ways suggests a short or touching probes; OL both ways may be an open device, poor probe contact or meter-setting issue. Diagnose actual readings before declaring failure. A forward-number/reverse-OL result is a basic low-current directional check only; it cannot establish rated power, authenticity, thermal margin or acceptance of the complete channel.

Primary references: [Fluke diode test method](https://www.fluke.com/en-ph/learn/blog/digital-multimeters/how-to-test-diodes), [TRR SR520–SR5200 datasheet, band/cathode convention](https://www.trrsemicon.com/Content/upload/pdf/202337086/SR5100.pdf?rnd=235). The datasheet is a family reference, not proof TRR manufactured the photographed part.

## Current Step 27 — lay out one motor channel, all power off, 5 November 2026

### Latest photo result and immediate checkpoint

Six originals plus observations are archived in [motor-review-2026-11-05](assets/motor-review-2026-11-05/manifest.json). Adapter label is now readable: MODEL1250, INPUT AC100–240V50/60Hz, OUTPUT12VDC5A, centre-positive. Label-implied power is60W. Accept these printed specifications and reported store voltage check without repeating earlier label/voltage questions. No actual loaded regulation, safety certification, barrel contact mapping or connector ampacity is proved by this photo. Motor reads JGB37-52012V22RPM. Fuse marking appears2, matching the planned2A selection; DC voltage/curve remain unknown. Module/connector match the previously reviewed forms.

**The red two-lead component in photo05 is an indicator LED (light-emitting diode), not the motor flyback rectifier.** Do not connect it across the motor. A flyback rectifier carries the motor's turn-off current to limit the resulting voltage spike; an indicator LED is not a substitute.

Next physical checkpoint, power off: locate the previously owned strip of black cylindrical axial diodes, illustrated in [the October photo](assets/inventory-2026-10-28/03-diodes.png). Choose one, keep it disconnected, and show its printed code and pale band. Expected selected code is SR5100; do not assign a rating/identity from shape alone. The pale band is the cathode-end identifier for this rectifier style; no installation orientation is issued yet. Wait for this identification before wiring. No new diode purchase, soldering, motor power or flash. Earlier missing-label requests below are superseded.

User reports the adapter was checked at the physical store and requests proceeding. Retain that report without repeating the same voltage test. Actual output current, connector polarity and scope of store testing are not supplied. Preparation can proceed while gathering those specifications; no powered wiring is issued.

1. Unplug Mega USB and the adapter from the wall. Keep the adapter output disconnected from all electronics and preserve the successful input/LCD wires.
2. Set out one existing JGB37-520 motor, one existing MOSFET module, one inline fuse holder with its intended fuse, one axial diode and the existing DC barrel/screw connector. Keep them electrically disconnected on a dry nonconductive surface. These form one motor channel: driver switches motor current, fuse protects a suitably matched branch, diode provides the designed path for motor turn-off energy, and connector brings in the low-voltage supply. Their suitability is not established solely by possession.
3. Request a clear photo of the laid-out parts, with close views or transcribed text for the actual fuse current/voltage markings and diode body code/band. Do not infer the delivered fuse is 2 A or diode is SR5100 from an order listing. No duplicate purchase or loose-driver resistance test is needed.
4. Ask the user to type the adapter's OUTPUT line (especially current in A) and state its printed connector polarity if readable. A photo is an alternative, not a repeated compulsory request. Explain that actual current and which output contact is positive are needed for the wiring/protection design; being store-checked does not tell this chat those facts. If the polarity symbol is unclear, request a close photo instead of guessing. No new energized measurement yet.

**Check before continuing:** wait for the parts/marking report. Do not connect motor, module or supply, assign output GPIO or upload firmware at this checkpoint. Next resolve the actual channel topology and matching fuse/diode/wire/connector ratings, secure the unloaded motor with shaft clearance and arrange independent accessible disconnection before safe-OFF/reset and powered tests. Breadboard/DuPont wiring is only for signals, never motor supply/return current. Earlier full-label/previous-probe questions below are superseded by this focused information request.

## Current Step 26 — adapter review after reconnection, 5 November 2026

**Reconnection result:** user reports all connected and working after Step 26D; accepts the restored USB logic/input circuit. LCD, buttons and index checks are user-reported, with no new serial capture/exact display trace or joint inspection. Earlier prompts below to reconnect, prove firmware retention or photograph the first solder joint are superseded. Preserve the current successful wiring and simulation; do not repeat the full historical tests without a new fault/change.

Next review is information-only, before motor power wiring:

1. Keep the adapter disconnected from the Mega, driver modules and motors. Unplug it from the wall before handling it for photographs. Do not open its enclosure or touch mains wiring.
2. Request a clear photo of its entire printed label, including model, INPUT, OUTPUT, current in A, any power in W and connector-polarity symbol. The earlier proposed 12 V / 5 A / 60 W is not the established rating of the delivered adapter.
3. Request a close photo of the output plug (tip/side) and any included detachable connector. A photograph alone cannot establish exact barrel dimensions or current suitability.
4. Credit the earlier user-reported 12 V DC reading. Ask whether the measurement was with nothing attached (unloaded), and whether the user remembers where the red/black probes touched and the reading's sign. Do not ask for another energized measurement yet; an unknown answer is acceptable and determines a later targeted check.

**Check before continuing:** wait for the photos/measurement explanation, then assess the actual adapter. No driver/motor connection, mains opening, output GPIO assignment or device command is issued. A 12 V reading does not verify current capacity, loaded regulation or connector polarity. Actual driver topology, motor wiring/connector/fuse/diode suitability, secured unloaded mount, accessible independent disconnect and safe OFF/reset handling remain later checkpoints before a protected single-channel test.

## Current Step 26D — reconnect three index switches, 5 November 2026

User reports buttons connected and requests proceeding. Accept that wiring report without repeating the first solder-joint checkpoint; no new solder/retention inspection or restored button function pass is inferred. Preserve LCD GND/5V/SDA20/SCL21, buttons D22/D23/D24 and existing shared GND. Mega retains simulation code by user report.

An index switch will eventually mark a dispenser's position. For now it is only a hand-operated simulation input. Each roller microswitch has COM (common contact), NO (normally open: closes to COM when pressed) and NC (normally closed: opens when pressed). Use the actual markings/previously identified contacts; physical terminal order is not universal.

1. Unplug Mega USB and all supplies before wiring. Leave the adapter, drivers, motors and fryer disconnected.
2. Identify switches 1/2/3 to match buttons 1/2/3. Connect each COM to the existing shared signal GND; leave any already-correct ground return in place.
3. Connect switch1 NO to Mega D26, switch2 NO to D28 and switch3 NO to D30. Follow printed numbers on the double-row header, one jumper per socket. Do not connect 5V to switch contacts.
4. Leave all NC contacts unused. Keep unused lugs and exposed joint metal from touching other conductors/case. Use secure individually insulated leads; if a connector will not stay attached or a label is unreadable, stop and report that rather than guessing.
5. Trace all six connections against [WIRING.md, Step 26D](WIRING.md#current-step-26d--three-index-switches-5-november-2026). Leave USB unplugged. No shared ground rebuilding or motor connections are needed.

**Check before continuing:** ask whether COM→shared GND and NO→26/28/30 are connected for all three, NC unused, with USB still unplugged. If they were already connected, accept an explicit mapping confirmation. Then issue a focused restored-circuit power/function check using the existing simulation; no automatic flash or repeat of the full historical fault-test suite.

## Current Step 26C — reconnect three flavor buttons, 5 November 2026

### Current sub-check: secure wire attachment before proceeding

**Latest clarification:** user has stranded 20 AWG wire and heat-shrink tubing, plus previously reported soldering gear. Earlier availability questions below are resolved. No soldering is yet reported complete. The first checkpoint is one joint, before assembling a whole button.

#### First physical checkpoint — one wire on one button contact

This joint replaces the slipping connector at the button. Later, the far end will receive a jumper-wire tail with a proper male pin; do not put bare 20 AWG into Mega/breadboard sockets or solder to Mega headers.

**Safety before starting:** unplug Mega USB and every supply. Disconnect both terminals of one red flavor1 button from all electronics so it is completely separate. Leave the LCD wires in place but unpowered. Work on a heat-resistant surface with a stable iron stand, eye protection and ventilation/fume extraction; keep your face out of the fumes. Secure the button in a suitable holder without crushing it, rather than holding the hot joint with fingers. Keep the hot tip/barrel off skin, insulation and button plastic. Use electronics-grade rosin/no-clean solder/flux, never plumbing acid flux. Wash hands after solder handling, especially with lead-containing solder.

1. Identify the two previously tested contact lugs. Either may receive this first lead: isolated contacts have no polarity. The old photo appears to show solder-style eyelet lugs, but gives no dimensions or heat limits. If the actual terminal is different or unclear, stop and send a close photo before heating it.
2. Cut one wire long enough to reach the intended controller area with a little slack. Leave the far end insulated and disconnected. Strip approximately 4 mm at the button end only, without nicking strands; gently twist the strands together. Adjust stripped length to suit the actual lug rather than leaving excess bare copper.
3. Slide an individual heat-shrink sleeve onto the wire before soldering and park it away from the hot end. It must pass over the finished lug/joint and later shrink snugly over the insulated wire; no exact tubing size is established. It must cover exposed metal and overlap insulation without blocking the button mechanism.
4. If the lug has a hole, pass the conductor through and form a gentle retaining hook. Keep every strand together and away from the other contact/case. Do not bend the lug, force an oversized bundle or cut strands off to make it fit. Report a fit problem before continuing.
5. Clean the iron tip and give it a thin coating of solder to aid heat transfer. Touch the tip to both wire and metal lug; feed a small amount of solder onto the heated joint so it flows onto both surfaces. Do not simply drop solder onto cold metal or make a large blob. No manufacturer heat limit is known for this generic button: if solder does not flow within a few seconds, remove the iron, let everything cool and investigate cleanliness/flux/iron condition rather than continuing to heat the switch. Stop for softened plastic, a moving lug or changed button action.
6. Remove solder wire, then the iron, and hold the joint still until solder sets. Let it cool naturally before handling. Inspect for solder bonded to wire and lug, no stray strands/bridges and no damaged plastic/insulation. Shine alone is not a quality test; lead-free solder can be matte.
7. Once cool, gently pull the insulated wire and press/release the disconnected button. The wire must stay attached without lug movement and the button must return normally. Leave heat-shrink back for a photo before covering the joint. Do not connect either end to electronics or power.

**Check before continuing:** request a close photo of this cooled joint and the gentle-pull/button-return result. Stop before the second lead, splices, heat shrinking or other buttons. Inspection cannot prove electrical contact action: after both leads are finished, the isolated button still needs a released-open / pressed-closed / released-open continuity test before electronics connection. No continuity mode on powered circuits.

User reports jumper connectors slipping off the button and asks about 20 AWG wire. A 20 AWG lead is electrically suitable for these very low-current contacts; larger wire does not fix an unsuitable connector. Stranded wire (many fine strands) is more flexible than solid wire (one conductor) for handled buttons. Before issuing cutting/soldering steps, ask which type they have and whether heat-shrink tubing and soldering equipment are available. Existing soldering-equipment ownership is recorded, but insulation availability is not.

Proposed approach, not yet selected or assembled: make a short wire lead (a pigtail) soldered to each suitable button contact, insulate each separately with heat-shrink, and splice its other end to a short jumper-wire tail retaining its factory male pin. This keeps a proper removable pin at the Mega/breadboard end. Support the insulated wire with slack so button movement cannot pull on the solder joint (strain relief). Do not solder wires directly to the Mega or force bare 20 AWG/strands or oversized solder-tinned ends into its sockets. Correctly sized removable crimp terminals are another option only after actual lug size and compatible wire/crimp tooling are established; do not guess a connector size from the old photo.

Future soldering checkpoint must start with USB/all supplies unplugged and button leads disconnected from electronics. Cover hot-iron burns, a stable iron stand, eye protection, ventilation/fume avoidance, hand washing after solder handling, and avoiding prolonged heat that can damage switch plastic. Stop after one insulated button assembly for inspection, gentle retention and isolated continuity checks before assembling the other two. No soldering/cutting or changed physical wiring is reported yet.

References: [Adafruit wire guidance](https://learn.adafruit.com/wires-and-connections/cables), [Adafruit breadboard jumper guidance](https://learn.adafruit.com/breadboards-for-beginners/diy-jumper-wires), [Adafruit insulated wire splices](https://learn.adafruit.com/lets-put-leds-in-things/soldering). These explain wire handling, not a verified thermal/terminal rating for the user's generic button.

User says the shared connections already exist. Keep the existing common signal ground; do not rebuild it or add a second rail. This report does not independently verify every return wire. LCD works and Mega sketch is unchanged by user report.

Each previously tested red button has two contact terminals. It is normally open (disconnected when released) and momentary (connected only while pressed). Either terminal can be the input; these contacts have no polarity. The existing simulation uses internal pull-up resistors: they hold each released input HIGH, and pressing connects it to GND, making it LOW. No external resistor or 5V contact wire is needed.

1. Unplug USB and every external supply before handling wires. Keep LCD connections intact and the adapter/motors/drivers disconnected.
2. Choose button identifiers 1, 2 and 3 consistently; label them if necessary.
3. Connect one contact of button1 to Mega D22, button2 to D23 and button3 to D24. Retain an already-correct signal wire rather than duplicating it.
4. Each button's other contact must connect to existing shared signal GND. Leave an existing correct return in place; add only a missing return. Do not attach either contact directly to 5V/VIN.
5. Trace endpoints using printed header numbers. The Mega's double-row connector can cause one-socket errors; do not assume 22/23/24 are all in one straight row. Use one jumper per socket and secure contact connections without adjacent bare metal touching. If a connection cannot be retained securely, stop and report it.
6. Leave USB unplugged and do not add index signal wires yet.

Table/diagram: [WIRING.md, Step 26C](WIRING.md#current-step-26c--flavor-buttons-5-november-2026).

**Check before continuing:** ask whether all three button connections match 22/23/24 with the other contacts on shared GND and USB still unplugged. Wiring completion is not a functional input pass. Index wiring and a focused restored-circuit check follow after the report.

## Current Step 26B — restore shared signal ground, 5 November 2026

**Step 26A result:** user reports LCD working after reconnection and confirms no different sketch was uploaded; only the breadboard was reused. Retained simulation firmware and LCD operation are user reports, not new tool captures. Keep the LCD's four connections and contrast setting intact.

Ground (GND) is the common electrical reference/return. The six input switches will each connect their input to this shared ground when pressed. A breadboard rail is a line of holes intended to share an internal metal contact; the blue/minus marking is only a guide and does not create a connection. Opposite rails and sections separated by a break may be isolated.

1. Unplug Mega USB and all supplies before moving wires. Leave the 12 V adapter, motors and drivers disconnected. Keep the LCD leads in place.
2. Identify one blue/minus-marked rail section with at least seven available holes for the ground feed and six future contact returns. Keep all seven within that one section; do not assume the rail continues through a central gap or connects to the opposite side. If its layout is unclear, ask for a photo review rather than guessing.
3. Fit one black male-to-male jumper between a **spare Mega GND socket** and a hole in that chosen rail section. Use one wire per Mega socket; do not stack it into the LCD's occupied GND socket. Follow printed GND labels, never adjacent 5V/VIN/RESET.
4. Leave the other parts disconnected and USB unplugged. No breadboard 5V supply is needed for these switch contacts, and motor return current must never use this rail.

See [WIRING.md, Step 26B](WIRING.md#current-step-26b--shared-signal-ground-5-november-2026) for the table and diagram.

**Check before continuing:** ask the user to confirm the GND jumper is connected, identify the chosen rail section, and confirm USB remains unplugged. Request a clear photo if the rail section or GND socket is uncertain. This connection report is not a measured continuity pass. Button reconnection follows after this checkpoint; restored input tests will check the paths functionally.

## Completed Step 26A — reconnect the LCD with all power off, 5 November 2026

**Result:** user reports LCD working and Mega code unchanged. The procedure and original pending prompt below are retained as history; proceed using Step 26B above.

The user removed the breadboard wiring for another project. Historical passes below do not establish today's connections. Whether the Mega received another sketch is unknown; ask before powering it. Restore one small section at a time and wait for the user's result.

**Before wiring:** unplug Mega USB and every external supply. Keep the 12 V adapter, motors, drivers and fryer disconnected. Work on a clean, dry, nonconductive surface. Never connect 12 V to the LCD or Mega 5V pin.

The LCD is the two-line display. Its attached rear I2C backpack reduces its communication wiring to two signals: SDA carries data and SCL carries the communication clock. VCC supplies power; GND is the electrical return/reference. Use the printed labels, not an assumed left-to-right order.

1. Take four male-to-female jumper wires: female sockets fit the LCD pins, male pins fit Mega sockets. If the ends do not fit securely, stop and report that.
2. Connect LCD GND to a Mega GND socket (black suggested).
3. Connect LCD VCC to the Mega POWER-header 5V socket (red suggested). Do not use VIN, RESET or 3.3V.
4. Connect LCD SDA to Mega digital 20 (blue suggested).
5. Connect LCD SCL to Mega digital 21 (yellow suggested).
6. Trace each wire end-to-end; check that connectors are not offset by one pin and bare pins do not touch. Leave the contrast trimmer unchanged. Leave USB unplugged.

Pin table and diagram: [WIRING.md, Step 26A](WIRING.md#completed-step-26a--lcd-reconnection-map-5-november-2026). These four wires connect directly; a breadboard is unnecessary for this checkpoint.

**Check before continuing:** ask the user to confirm the four connections are complete with USB still unplugged, and whether they uploaded different code to this Mega while using it for the other project. If unsure of endpoints, request a clear photo before power. No reconnection or powered result is recorded yet. Shared signal ground, buttons and index switches follow after this result; adapter review follows logic restoration. A fresh upload requires the project's normal explicit approval.

> **Current state, 5 November 2026:** Step24 USB-only logic checks passed; Step25 procurement review saved. Step26 is pending adapter label/polarity review. Adapter is now owned and user reports measured12V; current/power rating, polarity and loaded suitability are not yet established. October missing-adapter/pending-test statements below are historical. Driver GPIO and motor-power wiring remain unassigned. See [current handoff](handoffs/2026-11-05-assembly-resume.md) and [USB checkpoint](USB_LOGIC_CHECKPOINT.md).


Updated: **28 October 2026**, Asia/Manila.

The user explicitly authorised **Phase 2** with available materials. Outstanding purchases remain in the BOM; they do not prevent isolated unpowered input tests. We will complete one physical checkpoint at a time and wait for the user's observations before advancing. This guide does not authorise Phase 3.

## Completed Step 1 — three disconnected pushbuttons

### What this checks

A pushbutton is a manually operated electrical contact. Our intended flavour button is **normally open**: its two terminals are disconnected at rest. It is **momentary**: pressing connects them, and releasing disconnects them again. The red cap does not prove either behaviour; this test checks the delivered part.

**Continuity** means there is an electrical path between the meter probes. The meter supplies its own small test signal. A typical continuity setting beeps for a low-resistance path; the exact beep threshold depends on the meter. `OL` or an open-circuit indicator means no conducting path in this test.

### Safety before touching the probes

- Test **one loose pushbutton only**, disconnected from every other part.
- No USB, adapter, motor, capacitor or wall power is connected to this test.
- Put the black lead in **COM** and the red lead in the jack marked **V/Ω** or its meter-specific voltage/resistance equivalent. Do not use an A, mA or 10 A current jack.
- If the meter jack/mode labels are unclear, stop and ask for help identifying them rather than guessing.
- Do not perform resistance/continuity checks on powered circuits. Do not use this test on a household outlet or on a capacitor.

### Do this one component test

1. Take one red button out of its bag. Set it on a clean non-conductive surface. Its two metal terminals must be accessible and unconnected.
2. Select the meter's continuity/beeper setting. Some meters share this with diode/ohms mode and require a SELECT button; follow its actual labels. If there is no beeper function, resistance mode can show the same contact change.
3. Touch the probe tips together briefly. Note the beep and displayed resistance. This establishes that the meter/probes work and gives the shorted-probe baseline. Separate them; the meter should return to its open indication.
4. Touch one probe to each button terminal. Probe polarity does not matter for this isolated mechanical contact. Avoid letting the probe tips touch each other, which would create a false pass.
5. Observe with the button **released**, **held pressed**, then **released again**. Keep the probes in contact with the two separate terminals throughout. If convenient, repeat slowly to confirm the change is repeatable.

| Button state | Expected for the selected normally-open momentary type |
|---|---|
| Released | No beep; open indication such as OL |
| Held pressed | Beep; resistance close to the shorted-probe baseline |
| Released again | No beep; returns to open |

**Check before continuing:** Report the three states and the shorted-probe check. If readings are unstable, first check probe contact and mode. If it stays connected after release or conducts only while released, report the actual behaviour; do not assume the ordered contact type was delivered. Result recorded 28 October 2026: user confirms all three buttons matched the expected outcomes. All three pass this contact-action check; numeric resistance values were not supplied.

**Step 1 complete by user report.** No firmware or power supply was required.

Reference for the powered-off continuity method: [Fluke continuity testing guide](https://www.fluke.com/en-us/learn/blog/digital-multimeters/how-to-test-for-continuity). This is measurement guidance, not certification of the delivered parts.

## Completed Step 2 — disconnected microswitches

A microswitch is a small snap-action contact operated by a lever or roller. Here it will later signal a mechanism position to the Mega. A click alone does not prove an electrical connection.

### Identify the actual terminals

- **COM** or **C**: the common contact that switches between the other two.
- **NC**: normally closed, connected to COM when the lever is released.
- **NO**: normally open, disconnected from COM when the lever is released.

Read the markings moulded or printed beside the terminals; do not assign them by physical position or a generic diagram. If labels are unreadable, stop and send a clear close photo of the switch's marked sides and terminals.

### Safety and procedure

Keep the switch completely disconnected. No Arduino, USB, adapter, motor or capacitor connects to this test. Use the meter's black COM jack and red V/Ω jack, continuity mode; never a current jack. Only actuate the lever through its normal click/travel without bending or forcing it.

1. Take **one** loose microswitch. Confirm its COM, NC and NO labels.
2. Verify the meter by touching the probe tips together, then separating them.
3. Place the black probe on switch COM and red probe on switch NC. Keep tips separate. Observe released, gently held actuated, then released again: expected **beep → no beep → beep**.
4. Keep the black probe on COM and move the red probe to NO. Repeat: expected **no beep → beep → no beep**.
5. Record both sequences. A connected contact should read close to the shorted-probe resistance; exact meter beeper thresholds vary. Avoid resting fingers on exposed tips/contact surfaces if interpreting high-resistance readings.

**Result, 28 October 2026:** user confirms all switches work as intended following the issued check. Record the received microswitch batch as passing the reported COM–NC and COM–NO action checks. Exact switch count, individual labels and numeric resistance values were not supplied; do not substitute the planned quantity of seven for a counted quantity.

## Completed Step 3 — bare Mega USB power and detection

### What this checks

The Mega is the controller that will read switches, run the sequence and command driver signals. A USB connection can power the bare board and also carry programming/serial data. A lit power LED establishes only that power reaches the board; it does not prove data communication or our firmware.

### Check before applying power

1. Keep the board disconnected while inspecting it. Remove all jumper wires, shields and other modules from its headers. Look for loose wire strands, solder bridges between pins, debris, damaged connectors or obvious damage. If any is present, stop and send a photo.
2. Place the board on a clean, dry, nonconductive surface such as cardboard or a plastic stand. Keep it off metal and the outside of antistatic bags. Do not attach motors, drivers, the LCD, a barrel adapter or a bench supply.
3. Use a USB **data** cable that matches the actual board connector. The full-size Mega-style board normally has a square USB Type-B socket with two bevelled corners; the computer end must fit the computer directly. Do not force a plug. If the cable ends are unclear or do not match, send a photo of both ends before trying another connection. A cable supplying power alone is not proof it carries data.

### One physical checkpoint

Connect the bare board directly to the computer over USB only. Observe the ON/power indicator and any other LEDs. A preloaded L LED may blink or remain steady; do not require a particular blink pattern before our diagnostic is uploaded. Disconnect immediately if there is smoke, a burning smell or obvious abnormal heating; do not touch components to test their temperature.

**Result:** user reports ON lit and L blinking. Read-only host inspection now detects /dev/ttyUSB0, VID:PID 1a86:7523, product USB Serial, driver ch341-uart, readable and writable. Basic power/enumeration pass; no known-sketch upload or functional GPIO claim. Unpowered visual inspection was instructed but not explicitly reported separately.

### Linux baseline already checked (read-only)

On 28 October 2026, the agent ran:

```bash
command -v arduino-cli
command -v pio
command -v platformio
id -nG
ls -l /dev/ttyACM* /dev/ttyUSB* /dev/serial/by-id/* 2>/dev/null
```

No CLI executable path was returned for those three command names; this is a PATH check, not an exhaustive search for every installed IDE/tool. The current hans process already includes dialout. No matching serial device nodes were returned before this USB checkpoint. The listing's nonzero exit status reflected missing matches, not a diagnosed board failure. This baseline does not establish that a connected board is recognised.

After the user's USB result, read-only detection and port access checks succeeded as recorded above. No installation is needed for the initial power-light observation. Do not run sudo/usermod, install packages/cores or flash a device without presenting the exact commands and obtaining the user permission required by AGENTS.md. No dialout change is currently indicated. The complete diagnostic and build/upload instructions are now available and executed in Step 4; a power LED alone is not its success criterion.

References: [Arduino connection checks](https://support.arduino.cc/hc/en-us/articles/4412955149586-If-your-board-is-not-detected-by-Arduino-IDE), [Linux serial permissions](https://support.arduino.cc/hc/en-us/articles/360016495679-Fix-port-access-on-Linux). These support the method, not identification of the actual clone USB interface.

## Completed Step 4 — known diagnostic passed

The complete diagnostic source is saved in `firmware/mega_diagnostic/mega_diagnostic.ino`. Read [ARDUINO_SETUP.md](ARDUINO_SETUP.md) for exact proposed installation, compilation, port listing, upload and monitor commands, expected output, pinned versions and troubleshooting.

It uses only the built-in LED on pin 13 and USB serial: two short flashes every two seconds, a status line every second at 115200 baud, and an ACK when ? is received. Keep the board bare and USB-only. No external part is wired in this checkpoint.

User approved setup, compilation, diagnostic upload and serial capture. All completed successfully: checksum verified, 3334-byte program / 196-byte RAM build, verified upload exit 0, 27 consecutive heartbeat messages and ?/ACK reply. The serial monitor is closed; the program remains running. **Result:** user confirms the two short flashes and pause work as intended (28 October 2026). T04 complete; this checks the diagnostic and USB interface, not every GPIO or the entire machine. No external wiring yet. Logs/results are in .build/logs/; see TESTING.md.

## Completed Step 5 — LCD rear identified

The LCD is the screen for later countdowns and status. An **I2C backpack** is a small adapter board on the rear of some displays that lets the controller communicate through a four-pin connector. The received front photo does not show whether this adapter is installed or how its connector is labelled.

1. Unplug the Mega USB cable before any new handling or wiring. Leave all other supplies disconnected. The LCD must remain unpowered.
2. Turn the LCD over without removing or unsoldering anything.
3. Send a clear photograph of the **entire back**, especially any small adapter board, the pin labels beside its connector, the chip's printed marking and the soldered row joining the adapter to the display. If one photo cannot show the labels, add a close-up of that area.

Typical labels to look for are GND, VCC, SDA and SCL; these are examples only, not an instruction to assign positions or connect them. GND is the circuit return, VCC is the supply input, SDA carries communication data and SCL carries its clock. Actual labels, module identity and intended voltage must be reviewed before a pin table is issued. Do not infer voltage from VCC alone.

**Result:** rear photo now shows an attached HW-61 backpack, four-pin male header labelled GND/VCC/SDA/SCL from top to bottom in this view, and a blue trimmer. Chip text is not sufficiently legible to assign a precise IC, and no address/powered operation is yet checked. No additional backpack purchase is needed.

## Completed Step 6 — LCD wires connected, user report

An I2C link uses SDA (data) and SCL (clock); the display also needs supply and ground. The Mega uses digital **20 for SDA** and **21 for SCL**, verified against its official pinout. Use the complete pin table and diagram in [WIRING.md](WIRING.md), Step 6.

### Before connecting

**Unplug Mega USB and keep the barrel jack and every other supply disconnected.** Do not connect a 12 V adapter to this display or put its VCC on VIN. Keep motors, drivers and other modules disconnected. Leave the supplied trimmer and jumpers alone for this checkpoint.

1. Lay the LCD and Mega on a dry nonconductive surface, with their connector labels visible.
2. Take four male-to-female jumper wires. The female socket ends fit over the LCD pins; the male pin ends fit into the Mega's labelled sockets. Colours only help identify wires; actual endpoints matter.
3. Connect **LCD GND → Mega GND** (black suggested).
4. Connect **LCD VCC → Mega 5V** in the POWER header (red suggested). This is the planned 5 V LCD supply; keep it unpowered now. Do not use 3.3V, VIN, RESET or a numbered digital pin.
5. Connect **LCD SDA → Mega digital 20** (blue suggested).
6. Connect **LCD SCL → Mega digital 21** (yellow suggested).
7. Trace all four wires against WIRING.md; check each end seats securely on just one intended pin/socket. A breadboard is unnecessary for this direct connection.

**Result:** user reports “done, wires connected, proceed.” No wired photo was supplied, so do not claim an independent visual inspection. Use a final user-performed end-to-end label check before the next USB-only power observation. The existing diagnostic only drives the L LED and serial link; it cannot display countdown text.

No LCD power, I2C scan, library install, firmware flash or contrast adjustment has been performed. The generic display's exact electrical rating/IC is not independently established by its HW-61 marking; later powered-test acceptance will be kept distinct from this unpowered wiring step.

## Completed Step 7 — LCD USB-only first power observation

1. With USB still unplugged, trace the actual endpoints one last time: **GND → GND, VCC → Mega 5V, SDA → 20, SCL → 21**. Ensure sockets are not shifted by one pin and no adjacent exposed pins touch. Colours alone do not establish the connection. If an endpoint is uncertain, leave power off and ask for help/photo review.
2. Keep the barrel jack and every other supply disconnected; only the Mega and LCD are connected. Place both boards on a dry nonconductive surface.
3. Reconnect the Mega's USB cable to the computer. Observe whether the LCD backlight comes on. Disconnect immediately if there is smoke, a burning smell, abnormal heating or repeated power cycling; do not feel components to test their temperature or move wires while powered.

**Check before continuing:** report whether the LCD backlight illuminates, and whether you see blank space, dark blocks or any characters. No readable text is required yet: the currently uploaded Mega diagnostic does not initialise the LCD. A missing backlight is a symptom to investigate, not proof the whole LCD is faulty. Leave the contrast trimmer and backpack jumpers unchanged until the observation is reviewed.

**Result:** user reports “lcd working as intended, proceed.” The first power observation passes by user report; exact screen appearance was not specified and readable test text is not inferred. User directs continuation to the prepared address scan. Do not operate motors or connect another supply. The user requested proceeding after wiring; no extra permission is needed for this instructed low-voltage power observation.

### Address scanner — uploaded and passed in Step 8

`firmware/lcd_i2c_scan/lcd_i2c_scan.ino` is a complete, commented diagnostic for Mega SDA20/SCL21. It compiles with installed AVR Boards 1.8.8 and bundled Wire; no additional library installation. It performs an address-only scan at 100 kHz, reports responding addresses over serial at 115200 baud, has a 25 ms Wire timeout and stops on a held-low bus/transaction fault. Send r to repeat. It does not initialise LCD text or claim an address before measurement.

Compile-only command already run:

```bash
cd /home/hans/repos/fries-machine
bash -c 'source tools/arduino-env.sh
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" compile --fqbn arduino:avr:mega:cpu=atmega2560 --warnings all --build-path "$FRIES_PROJECT_ROOT/.build/lcd_i2c_scan" "$FRIES_PROJECT_ROOT/firmware/lcd_i2c_scan"'
```

Compile log: `.build/logs/lcd-i2c-scan-compile.log`. Compilation alone did not communicate with the board. Following the user's power confirmation/proceed instruction, the prepared scanner was uploaded with --verify (exit 0); two scans each found 0x27, one device, no scanner error. Serial log/result are in .build/logs/.

## Completed Step 8 — address confirmed; text test prepared

Scanner startup and r rescan both reported **FOUND 0x27 / SCAN_COMPLETE devices=1** at 115200 baud. The monitor is closed. This confirms the backpack responds at that address, not that LCD characters render correctly.

The complete next sketch is `firmware/lcd_text_test/lcd_text_test.ino`; [LCD_TEST.md](LCD_TEST.md) contains exact proposed commands and expected output. It will show FRIES MACHINE and advancing Seconds: using the same wiring. It uses **hd44780 by Bill Perry 1.3.2**, which is not yet installed; this library configures the expander-to-LCD mapping at the measured address. It handles init/write/timeout errors and drives no actuators.

The user explicitly approved the concrete library/text-test execution with “proceed.” It has now been installed/compiled/uploaded and serial-checked in Step9; no further permission for that completed action is pending. No hardware connection change needed. See LCD_TEST.md for exact commands and evidence.

## Completed Step 9 — LCD text and contrast check passed

Approved execution passed: hd44780 1.3.2 installed project-locally; Mega compilation succeeded (10574 bytes flash /511 bytes RAM); upload with verification exited0. Serial reported LCD_TEXT_TEST_V1 READY and 27 increasing seconds values without a reported LCD error. Monitor is closed; text diagnostic remains running.

Keep the same USB-only Mega/LCD wiring. **Actual observation:** user reports nothing appears; photos show a lit blue screen without readable characters. Visual text check has not passed. Successful API/serial output is not independent proof of visible characters.

Next one physical check: adjust the blue rear contrast trimmer gently while running the existing USB-only text test. Full beginner procedure and short-circuit precautions are in LCD_TEST.md, current Step9 troubleshooting. Watch for letters or filled character rectangles. Keep wiring/jumpers unchanged, do not force the trimmer, and report the result before any further step.

**Result:** user confirms “now working as intended” after the contrast check. Photo17 clearly shows FRIES MACHINE and Seconds:23. The reported contrast adjustment resolved visibility without a new code upload. LCD text test passed; retain its setting. This is not cooking firmware or a Phase3 transition.

## Completed Step 10 — three flavour-button connections reported

Each red pushbutton is a normally-open momentary contact: it connects its two terminals only while held. We will use the Mega's internal pull-up resistors in the next input-test program, so each button connects a digital input to GND. A pull-up is a weak internal connection that holds the unpressed input HIGH; pressing makes it LOW. No added resistor or 5V wire goes to these button contacts.

1. Unplug USB and every other supply. Leave the four working LCD wires in place; no driver or motor is connected.
2. Identify the Mega's **digital22,23,24** labels. They are in the double-row digital connector, not the numbered analog header. The exact printed numbers determine the socket, not a guessed left/right row.
3. Connect one terminal of button1 to **22**, the other to an unused **GND** socket.
4. Connect button2 similarly to **23** and another unused **GND** socket.
5. Connect button3 similarly to **24** and another unused **GND** socket.
6. Use one secure wire per Mega socket. Each button's two contact terminals can be exchanged; these switches have no polarity. Do not put a button terminal directly on5V/VIN. See WIRING.md Step10 for colours, purposes and full ASCII diagram.

**Check before continuing:** trace all six endpoints and report the three buttons connected, leaving USB unplugged. A photo is useful if connector positions are unclear. If jumper ends do not fit the button terminals, stop and show/describe them before soldering or improvising. Keep motors and their supplies disconnected.

### Connector retention question — current Step10 sub-check

User asks how to keep fitting jumpers attached. Keep USB unplugged. If a jumper seats snugly and proper electrical tape is available, retain each connector separately and anchor its insulated wire to the stationary button body/support with slack. This strain relief prevents button presses pulling on the contact. Tape is not a fix for loose/intermittent electrical contact. Try one unpowered lead first and report gentle-pull retention/free-button action; full advice and durable alternatives are in WIRING.md, Keeping the prototype button leads attached.

Suitable solder-terminal pigtails with individual heat-shrink are the durable alternative, after confirming terminals/insulation. No cutting/soldering or new purchase directed now. Keep Mega-side connections removable; anchor cables instead of soldering/gluing sockets.

User now reports all buttons connected and says proceed. Matching input diagnostic has been prepared/compiled/uploaded in Step11 using already installed Wire/hd447801.3.2. No independent photo of all six endpoints was supplied; do not infer physical input passes from the completion report.

## Completed Step 11 — flavor-button input test, user report

The user requested proceeding after connecting all buttons. Uploaded complete firmware/flavor_buttons_test with 35ms software debounce and startup-held protection. Host timing tests and Mega compilation passed (11692 flash /584 RAM bytes); verified upload exited0. Serial READY and14 idle samples show raw111, counts0,0,0, lcd=OK, no errors/held inputs. Monitor closed; tester running. Existing libraries reused; no new installation.

Read [BUTTON_TEST.md](BUTTON_TEST.md) for complete expected output, commands and limits. LCD initially shows BUTTON TEST / Press1,2or3 (with normal spaces).

1. With USB-only power and unchanged secure wiring, press/release **button1**: expect FLAVOR 1 and its Count increasing by1.
2. Press/release **button2**, then **button3**, separately: expect FLAVOR 2 and FLAVOR 3 respectively, each with its own count.
3. Hold any one button for about2seconds: its count increases once, not continuously. Release, wait a moment, and press again: it increases once more. The last selection remains on screen after release.

**Check before continuing:** report whether each button selects the matching number and whether holding counts only once. Do not change wires while powered. If a mapping/contact is wrong, record which input and what LCD shows; unplug before corrections. Do not add index switches or motor drivers until these results are reviewed. These are test identifiers, not assigned real flavour names or active dispensing/cooking commands.

**User result, 28 October 2026:** User initially questioned the double-row header positions, then reports: “nevermind, fixed it myself, all buttons working as intended, proceed.” Record the three-button input test as passed by user report after a self-corrected connection. Exact changed sockets, individual count values and a separately itemised physical held-button result were not supplied; do not invent them. Recheck held-input behaviour during later integration.

## Completed Step12 — module identification and user test report

A MOSFET module is an electronic switch: a small controller signal controls a separate motor-power circuit. The selected BOM family is LR7843, but actual terminal labels and board layout must be inspected before assigning wires. A component name alone does not establish a module pinout or an adequate flyback-current path.

1. Unplug Mega USB and disconnect every external supply before handling or moving connections. Keep the successful LCD/button wiring in place.
2. Set **one loose soldered MOSFET module** on a nonconductive surface. Do not connect it to the Mega, a motor or a power supply yet.
3. Supply clear photographs of its component/label side and underside/solder joints. Include the whole module and all terminal markings. If a marking is unreadable, report that rather than assigning a terminal by position.

**Check before continuing:** review the user's actual module labels, connector assembly and visible solder joints before issuing its connection table. A photograph can reveal obvious bridges or loose joints but cannot certify electrical operation. Ask whether the regulated 12 V motor adapter is already in hand; obtain its label and measured output/polarity at a later power-supply checkpoint. No driver GPIO is assigned and no wiring, installation, flash or motor-power test is issued at Step12. The current button tester stays uploaded; no software change is needed for this identification step.

**Photo review received:** one module shown on both sides, labels PWM/GND and +/LOAD/− readable. See WIRING.md Step12 photo review for orientation, terminal roles and limits. No obvious adjacent-net solder bridge visible; electrical condition untested.

### Current Step12 checkpoint — resistance across disconnected power terminals

**Before using resistance/continuity mode:** module must have no wires attached, no motor, no adapter and no Arduino connection. Unplug Mega USB before handling nearby wiring; keep successful LCD/button leads unchanged. Never use resistance mode on a powered circuit. This check concerns the loose driver only, not the power adapter or mains.

1. Black meter lead in **COM**; red in **V/Ω**, never the A/mA current jack. Select **Ω (resistance)**, with auto-range or a suitable range if available.
2. Touch the probe tips together briefly and note the near-zero lead reading; separate them. This gives a reference for a direct metal short.
3. Touch **red to the module's + terminal** and **black to its − terminal**. Use the underside markings to identify the corresponding top screw/terminal metal. Keep tips apart; do not bridge an adjacent terminal.
4. Wait a few seconds and report the displayed number **and unit/range**, or OL. Report if the reading starts low then rises. If the meter has only continuity, report whether the beep persists or is brief instead; no resistance value may be inferred from a beep alone.

```text
Meter COM -- black probe -------- module −
Meter V/Ω -- red probe ---------- module +
Module PWM / GND / LOAD: empty. Module entirely disconnected.
```

**Check before continuing:** request the measured reading and whether the regulated12V motor adapter is already in hand (label photo if present). A persistent reading near the shorted-probe baseline is suspicious: do not power the board; review the measurement and joint details first. A higher reading or OL only rules out an obvious direct short in this measurement; it does not verify driver switching, safe OFF/reset, current capacity, isolation or flyback protection. No exact nominal resistance is assumed without the actual circuit. Stop here for the user's result. No wiring to a GPIO, installation, upload or motor-power operation is issued.

**Subsequent user result:** User reports all MOSFET modules were already checked and are working. Accept this as a user-reported functional check; test method, readings and total count were not supplied. Do not repeat the requested resistance test or claim measured current, safe OFF/reset, thermal or loaded-motor qualification. User explicitly confirms the 12 V motor adapter is not yet owned. The earlier requested resistance reading is not repeated.

## Completed Step13 — one roller microswitch connected, user report

The missing motor adapter does not prevent a controller-input test. Leave motor drivers and motors disconnected. A microswitch is a mechanically operated electrical contact. This first switch will represent **flavor-coil index1**: a reference position the coil will later reach once each turn. This test uses hand operation only; it does not prove one-packet dispensing or mechanical index placement.

**Before changing wires:** unplug Mega USB and all other supplies. Keep the successful LCD/button wiring unchanged. Use the switch's actual COM/NO/NC markings and the earlier contact checks; do not assume the middle physical lug is COM. If labels cannot be read, obtain a clear view before wiring.

| Component terminal | Mega pin | Suggested wire colour | Purpose |
|---|---|---|---|
| Microswitch COM (common) | An unused socket explicitly marked GND | Black | Circuit return when the NO contact closes |
| Microswitch NO (normally open) | Digital26 | Blue | Future index1 input; goes LOW when lever is actuated with INPUT_PULLUP enabled |
| Microswitch NC (normally closed) | No connection | None | Not used in this isolated NO-contact diagnostic; keep clear of other conductors |

```text
Mega D26 ---- NO  [roller microswitch]  COM ---- Mega GND
              NC: no wire
LCD remains GND/5V/SDA20/SCL21.
Buttons remain D22/GND, D23/GND, D24/GND.
USB and external supplies unplugged during wiring.
All motor/driver connections remain absent.
```

1. Select **one** previously contact-tested roller microswitch and identify COM and NO from its markings/known meter test. NC is the other labelled contact and stays empty.
2. Attach a snug, insulated signal lead from COM to an unused labelled Mega GND socket. If there is no free GND or the connector does not fit securely, report that before improvising a shared connection.
3. Attach NO to **D26**. In the pictured double-row header, D26 is in the same inner row as22 and24, immediately after24; opposite it is27. Skip the extra5V pair at the header end. Use printed numbers.
4. Ensure the NC lug and exposed lead metal cannot touch adjacent terminals. Lightly operate the lever without pulling on the leads.

**Check before continuing:** leave USB unplugged and report this one switch connected (or send a clear terminal/header photo if uncertain). Do not power or upload yet. D26 is now reserved for this next diagnostic, but the currently uploaded flavor_buttons_test only reads22/23/24 and will not display index events. Matching complete input/index firmware is the next software checkpoint after wiring confirmation, with the required upload permission handled then. No firmware/pin change has been made to the running button diagnostic.

The later input test will enable the Mega's internal pull-up on26: lever released = HIGH; lever actuated = LOW. Mechanical contact bounce will be filtered in software, just as for the red buttons. A broken wire can also read HIGH in this NO arrangement; this is a bench input test, not a fail-safe limit or emergency-stop circuit. Final homing/index timeout and any NC fault-detection arrangement must be designed and tested separately.

References: [Arduino internal pull-up example](https://docs.arduino.cc/built-in-examples/digital/InputPullupSerial/) and [Mega pinout](https://docs.arduino.cc/resources/pinouts/A000067-full-pinout.pdf). No new parts, packages or prices are introduced by this wiring step.

**User result:** “connected.” Recorded as completed wiring report; no physical index input event verified.

## Completed Step14 — index1 input passed by user report

User reports Step13 COM/GND–NO/D26–NCempty switch connected and subsequently explicitly approved the prepared diagnostic upload. Keep the existing buttons/LCD unchanged. Complete `firmware/inputs_index_test` now runs; exact commands and logs in [INDEX_TEST.md](INDEX_TEST.md).

Compile passed11922 flash/599RAM bytes; identical debounce-helper host tests passed. Pins22/23/24/26 use INPUT_PULLUP; LCD0x27/SDA20/SCL21 unchanged. No motor/driver/heater outputs configured.

User approved the prepared upload with “proceed.” Rechecked /dev/ttyUSB0 USB1a86:7523 and read/write access; source hashes matched compiled source. CLI upload --verify exited0. Serial INPUTS_INDEX_V1 READY plus 16 released-idle samples raw1111/counts0,0,0,0/lcdOK; no LCD error, held-at-boot tag or physical input press during capture. Unreadable startup bytes preceded clean tagged output. Monitor closed Ctrl+C exit0; inputs_index_test now runs on the board. No package install or wiring change. Physical lever test remains pending.

**Check before continuing — operate only the roller lever, do not move wires:** hold about2seconds; expect INDEX 1: ACTIVE and exactly one Count increment. Release: INDEX 1: READY with Count unchanged. Press/release again: one additional count. Ask user for actual visible states/count behaviour and wait. Do not infer physical contact closure from idle1111. No new installation/upload or connection needed for this observation.

**Step14 user result:** User replies “working as intended” to the explicit Step14 lever-hold/release/repress checklist. Record INDEX1 onD26 ACTIVE/READY display, one count per hold, unchanged count on release and another count on repress as PASS by user report. Numeric final count and a serial capture of these manual events were not supplied; do not invent them. This is an input test, not mechanical dispensing or a motor test.

## Superseded Step15 proposal — user already has common signal ground

Step14 first index-switch input passed by user report. Before adding two more switches, provide a shared GND connection without placing multiple wires into a single Mega socket. The existing direct LCD/button/index connections use several ground sockets. A **breadboard power rail** is a long connection strip for distributing one electrical connection; its printed colour is only a label, not proof of electrical continuity. Some rails are split.

**Safety before this check:** unplug Mega USB and every other supply. Use an otherwise empty breadboard rail; do not connect it to the Mega or change the successful wires yet. Resistance/continuity mode must never be used on a powered circuit.

1. Find one clearly marked long power rail, preferably beside a blue line or minus sign. Select **four nearby holes along that same rail**, calling them1–4 from one end. These will later accommodate MegaGND plus the three microswitch COM leads. Do not choose holes across the central breadboard gap or jump to the opposite rail.
2. Meter black lead in COM and red lead in V/Ω; select continuity/beeper mode. Verify the meter beeps when probe tips touch. Use snug male jumper pins in the chosen holes to make probe contact; do not force thick meter probes into breadboard sockets.
3. With one jumper in hole1 for the black probe, put a second jumper in hole2 and touch its free conductor to the red probe. Check for a steady beep. Move only that second jumper to hole3, then hole4, checking each against hole1.

```text
ISOLATED, UNPOWERED breadboard rail:
Chosen holes:      1    2    3    4
Meter black ------1
Meter red -------------2    (first check)
                        3    (second check, against1)
                             4 (third check, against1)

No Mega/switch/supply connected to this rail yet.
```

| Test | Expected | What it establishes |
|---|---|---|
| Hole1–hole2 | Steady continuity beep | Same electrical group |
| Hole1–hole3 | Steady continuity beep | Same electrical group |
| Hole1–hole4 | Steady continuity beep | Same electrical group |

**Check before continuing:** report whether all three pairs beep. If any fail, report which pair or show the breadboard before moving wires; a split rail or different connection group may be involved. Wait for this result before using that group as shared ground. Existing working LCD, three buttons and D26 switch remain unchanged and unplugged for this checkpoint. No new index GPIO, firmware, upload or motor-power operation is issued yet. The next step will connect the verified ground group and the remaining index switches, then prepare a matching diagnostic. Shared-ground rail is for low-current input signals only, not motor current.

**Step15 user clarification:** User states an existing common breadboard GND line is already made for everything and supplies photo21. Accept the existing signal-ground arrangement as user-reported; retain it instead of building a second rail or repeating the empty-rail procedure. Photo shows multiple jumpers near the blue marking but does not prove every endpoint or split-rail continuity. Earlier working LCD/buttons/index1 support those tested signal paths, not every unused rail hole. No numeric continuity reading or new meter pass is inferred.

## Completed Step16 — switches2/3 connected by user report

The user already has common ground; Step15's proposed empty-rail construction is superseded. Reuse the **same connected ground section** already used by the working input circuit. Printed colour and wire colour do not determine electrical identity. Do not connect a separate rail segment on the assumption it is internally continuous.

**Before moving/adding wires, unplug Mega USB and every other supply.** The photograph shows ON lit, so ensure USB is now actually disconnected. Preserve the LCD, three buttons and working index1 connection. Motor drivers/motors remain disconnected; breadboard ground is for these low-current control/input circuits, not motor-current routing.

| Component terminal | Mega / shared-ground connection | Suggested wire colour | Purpose |
|---|---|---|---|
| Index switch2 COM | Existing connected signal-GND rail | Black | Common return, linked to MegaGND |
| Index switch2 NO | Reserved digital28 | Yellow | Future flavor-coil2 reference-position input |
| Index switch2 NC | No connection | None | Unused in this NO-contact input diagnostic |
| Index switch3 COM | Existing connected signal-GND rail | Black | Common return, linked to MegaGND |
| Index switch3 NO | Reserved digital30 | White | Future flavor-coil3 reference-position input |
| Index switch3 NC | No connection | None | Unused in this NO-contact input diagnostic |

```text
Existing MegaGND ---- existing connected signal-GND rail
                         |---- COM index1, NO ---- D26 (already tested)
                         |---- COM index2, NO ---- D28 (new)
                         |---- COM index3, NO ---- D30 (new)
NC on each switch: unused. LCD/buttons unchanged.
```

1. Identify COM/NO/NC from each previously tested switch's actual markings. The middle physical lug is not assumed to be COM.
2. Add switch2 COM to an available hole on the existing connected GND section and NO to **D28**.
3. Add switch3 COM to that same connected GND section and NO to **D30**. Keep both NC terminals empty and exposed conductors separated; use snug, insulated leads as for the first switch.
4. D26, D28 and D30 are consecutive sockets along the same **inner/even-numbered** row. Their opposite sockets are27,29,31. Use printed labels, leaving existing D26 untouched.

**Check before continuing:** leave USB unplugged and report both new switches connected, or report a terminal/ground-section uncertainty before improvising. Do not change the working circuit or build another ground rail merely to follow earlier assumptions. Current uploaded inputs_index_test reads only22/23/24/26; **D28 andD30 are reserved for the next diagnostic and will not display events yet**. Matching all-three-index firmware follows the wiring report; no new firmware or upload is issued here. Final machine fault detection/homing mechanics and all motor-power tests remain separate.

**Step16 user result:** “done, connected.” Connection completion reported; switch2/3 physical input events not yet tested.

## Completed Step17 — all three flavor-index inputs passed by user report

User approved the prepared upload. IndexNO26/28/30 and COMexistingGND/NCempty, buttons22/23/24 and LCD0x27/SDA20/SCL21 unchanged. Complete `firmware/inputs_three_index_test` now runs. [THREE_INDEX_TEST.md](THREE_INDEX_TEST.md) has exact commands and manual checks.

User approved the prepared three-index diagnostic upload with “proceed.” Rechecked /dev/ttyUSB0 USB1a86:7523, read/write access and unchanged source hashes. CLI upload --verify exited0. Serial INPUTS_3INDEX_V1 READY and15 released-idle samples raw111111/counts0,0,0,0,0,0/lcdOK; no LCD_ERROR, HELD_AT_BOOT or physical press during capture. Startup unreadable bytes preceded clean tags. Monitor closed Ctrl+C exit0; inputs_three_index_test now runs. No new library, wiring change or actuator output. Physical three-index mapping/hold/release and button regression remain pending.

Compile/host evidence remains PASS12054flash/619RAM, identical debounce helper; four supplied-core warnings only. All six inputs use INPUT_PULLUP. Current firmware now reads28/30; no further flash or connection required for manual testing.

**Check before continuing:** operate levers1,2,3 individually, keeping others released. Each should show its own INDEXnumber ACTIVE and exactly one increment during a2second hold; release shows same index READY with count unchanged; repress adds one. Then recheck buttons show matching FLAVOR1/2/3. Ask actual results and wait before adding anything else. Do not touch wiring while powered. No motor power or Phase3.

**Step17 user result:** User reports “all microswitches working as intended” after the Step17 three-lever mapping/ACTIVE/READY/hold/release/repress checklist. Record all three connected flavor-index inputs26/28/30 as PASS by user report. Exact final counts and manual-event serial traces were not supplied. The user did not separately confirm the requested three-button regression on this latest six-input upload; earlier button checks remain passed. Do not extend this report to unconnected basket switches or powered/mechanical indexing.

## Completed Step18 — only three microswitches owned

The three connected flavor-index inputs passed Step17 by user report. Preserve the working LCD/buttons/index wiring and inputs_three_index_test. The12V motor adapter is explicitly not yet owned, so no powered driver/motor test is issued.

The BOM provisionally plans **seven microswitches total**: three coil indexes plus four basket end-position inputs. Those four cover the two ends of the proposed lift and tilt axes; actual mechanical mounting, final function and any NC/fault-detection arrangement remain subject to the retained PDF mechanism. A future hand-operated input check would not authorise basket motion or determine safe mounting.

**Current missing information:** does the user have **four additional roller microswitches**, besides the three now connected? Ask for availability/remaining quantity; do not assume planned shopping quantity equals received count, declare them missing, or order duplicates. If available, next prepare an unpowered bench-input connection checkpoint using actual terminal labels and a matching diagnostic. If fewer, record the count and choose useful firmware/input work with present hardware before purchasing. No new GPIO assignment, firmware, connection or upload yet.

**Check before continuing:** wait for the user's quantity response before the basket-input wiring branch. No action on the working hardware is required now. All current driver and basket pins remain unassigned. Adapter purchase remains the already documented regulated12V5A enclosed unit on the physical-store list, with actual label/output/polarity/protection verification needed before motor power. No new price or purchase item is introduced.

**Step18 user answer:** no additional switches; only the three connected switches. Four provisional basket switches remain to buy; no basket GPIO assigned.

## Completed Step19 — first physical simulation passed by user report

Retain current six inputs/commonGND/LCD; no new wires. Complete `firmware/cycle_logic_test` now runs and has **no actuator output pins/API**. [CYCLE_LOGIC_TEST.md](CYCLE_LOGIC_TEST.md) contains exact commands and expected sequence.

User approved the prepared control-logic simulation upload with “proceed.” Rechecked /dev/ttyUSB0 USB1a86:7523 and read/write access; all source hashes unchanged. CLI upload --verify exited0. Serial CYCLE_SIM_V1 READY and17 idle samples phaseIDLE/flavor0/seconds0/raw111111/lcdOK; no LCD_ERROR, HELD_AT_BOOT or physical contact event during capture. Partial/duplicate boot text preceded stable tagged startup/status. Monitor closed Ctrl+C exit0; cycle_logic_test now runs on the Mega. No library install, wiring change, motor/heater outputs or manual simulated sequence performed.

Host logic/debounce tests and build remain PASS13360flash/797RAM,4corewarningsonly. This is a software/input simulation, not a powered prototype or actual cooking recipe. Four basket switches and12Vadapter still missing.

**Check before continuing:** with all contacts released, press/release flavor2 then hand-operate index2/D28 within15seconds. Expect selected Flavor2, SIMWARMUP5s, SIMCOOK10s, then SIMTIMERSDONE/Basketpending. Ask for actual display sequence and wait before fault/busy/recovery tests or further hardware. All drivers/motors/heater/external supplies remain disconnected; no movement expected. If timeout, report actual display/contact before changing anything. Keep powered wiring untouched.

**Step19 user result:** User replies “yes, working as intended” to the first Step19 manual flavor2→index2/D28→SIMWARMUP5s→SIMCOOK10s→SIMTIMERSDONE/Basketpending checklist, retainingFlavor2. Record PASS by user report; no stopwatch measurements or manual-event serial capture supplied. This validates the software/input simulation only, not physical dispensing, heating or basket movement.

## Completed Step20 — busy-button selection lockout passed by user report

Step19 first manual simulation passed by user report. Keep the same uploaded cycle_logic_test and all existing wiring; no new firmware/connection or device command is needed. Drivers/motors/heater/external supplies remain disconnected, USB logic power only.

Read these steps before starting, so the short simulated cooking window is clear:

1. Release all buttons/levers, then press the Mega's small onboard **RESET** button once. Wait for **SIMULATION ONLY / Select flavor**. This is a bench simulation reset, not a real machine emergency stop.
2. Press/release **flavor button1**. Within15seconds press/release **index1/D26**, just as the prior test used flavor2/index2.
3. Wait through the5second SIMWARMUP until **SIM COOK** starts its10second countdown.
4. During SIMCOOK, press **flavor button2**, hold about2seconds, then release. Press/release **flavor button3** while the countdown is still active. Expect **Flavor1** to remain selected and remaining seconds to keep decreasing; no switch toFlavor2/3 or restart to10s/5s.
5. At **SIM TIMERS DONE / Basket: pending**, press/release button2 once. Expect the stopped completion view to remain; busy presses must not have queued another simulation, and this diagnostic needs an explicit reset for another run.

**Check before continuing:** ask whether Flavor1 remained selected, timers continued without restarting and the final view stayed stopped after the extra press. Wait for that physical result before wrong-index/timeout/reset tests or further code/hardware. Do not touch wiring while powered. If any selection/timer changes unexpectedly, report which button and LCD stage/countdown; do not rewire or reflash automatically. Host lockout tests passed previously, but this actual input/LCD lockout check is still pending.

**Step20 user result:** User confirms “yes, working as intended” to Step20: flavor1/index1 starts the simulation; button2 held and button3 pressed during SIM COOK do not change Flavor1 or restart the countdown; the final Basket: pending view remains latched after another button2 press. Record busy-selection lockout and no queued restart as PASS by user report. No manual-event serial capture or stopwatch timing supplied; no physical motor/heater test inferred.

## Completed Step21 — wrong-index rejection and flavor3 passed by user report

Step20 busy-button check passed by user report. Keep the existing uploaded cycle_logic_test, six input wires and LCD unchanged. This is still an output-free USB-only simulation; motors, drivers, external supplies and heater remain disconnected.

Read the sequence before starting: all index responses below must fit inside the same15-second response window.

1. Release every button/lever, press the Mega's small onboard RESET button once, and wait for SIMULATION ONLY / Select flavor.
2. Press/release **flavor button3**. Expect SIM PRESS INDEX / Flavor3 with the response countdown.
3. Briefly press/release **index1/D26**, then **index2/D28**. These are roller levers, not flavor buttons. Expect the display to stay on SIM PRESS INDEX / Flavor3 while the countdown continues; neither wrong index may advance or restart it.
4. Before that same15-second window expires, press/release **index3/D30**. Only this matching index should advance to SIM WARMUP5s, then SIM COOK10s, then SIM TIMERS DONE / Basket: pending, retaining Flavor3.

**Check before continuing:** ask whether indexes1/2 were ignored and only index3 advanced the Flavor3 simulation through the timers. Wait for this physical result before timeout/recovery or initially-held-index tests. If the window expires, get the actual display and sequence rather than assuming wrong-index rejection failed. No reflash, serial monitor opening, wiring change or further part purchase is required for this observation. RESET is a bench reset, not an emergency stop.

**Step21 user result:** User reports “working as intended” after Step21: flavor3 stays waiting when index1/D26 and index2/D28 are operated, then only matching index3/D30 advances through the simulated timers to Basket: pending. Record wrong-index rejection and Flavor3 sequence as PASS by user report. No independent timing measurement or manual-event serial capture supplied; this remains a software/input test.

## Completed Step22 — timeout/fault/reset passed by user report

Step21 wrong-index test passed by user report. Use the same cycle_logic_test and unchanged wiring with USB logic power only. All motors/drivers/heater/external supplies remain disconnected. This checks the software's missing-response path, not motor jam/stall protection or an emergency stop.

1. Release all buttons/levers, press the Mega's small onboard RESET button once, and wait for SIMULATION ONLY / Select flavor.
2. Press/release **flavor button2**, then **do not operate any roller lever**. Allow its15-second index-response countdown to expire.
3. Expect **SIM FAULT / INDEX TIMEOUT**. No SIM WARMUP or SIM COOK stage should start.
4. While the fault is displayed, press/release **index2/D28**, then **flavor button1**. Expect the fault to remain: a late index or new selection must not resume/restart the simulation.
5. Release every control and press onboard **RESET** once. Expect **SIMULATION ONLY / Select flavor**, remaining idle without a new button press.

**Check before continuing:** ask whether the missing response produced the fault, the fault stayed after the extra switch/button presses, and RESET returned to idle. Wait for that result before initially-held-index/startup-input tests or any further code/hardware. No new upload, serial monitor opening or wiring change needed. If behavior differs, request the actual display/operation sequence; do not infer a defective switch or alter powered wiring. Reset here is a bench software reset and does not qualify a physical safety-stop circuit.

**Step22 user result:** User confirms “yes, working as intended” to Step22: omitting the selected index response produces SIM FAULT / INDEX TIMEOUT; a late index2 actuation and new flavor1 press leave the fault latched; releasing controls and pressing RESET returns to idle. Record timeout, fault latch and explicit-reset recovery as PASS by user report. No stopwatch or manual-event serial measurement supplied; this does not qualify motor jam protection or a physical safety stop.

## Completed Step23 — initially-held selected-index check passed by user report

Step22 timeout/fault/reset test passed by user report. Preserve the uploaded cycle_logic_test and successful six-input/LCD wiring. Use USB logic power only; all motors/drivers/heater/external supplies stay disconnected.

Read the sequence before starting; release/re-actuation must occur within the15-second response window that begins at flavor selection.

1. Release all controls, press the Mega's small onboard RESET button once, and wait for SIMULATION ONLY / Select flavor.
2. Press and **hold index1/D26** for about1second before selecting a flavor, allowing its contact filter to settle.
3. Still holding that roller lever, press/release **flavor button1**. Expect **SIM RELEASE IDX** with Flavor1. Keep the lever held about2seconds: warm-up must not begin from the old active index state.
4. Release index1. Expect **SIM PRESS INDEX**, still Flavor1 and inside the same countdown; release alone must not start warm-up.
5. Press/release index1 again before the original15-second window expires. Only this fresh actuation should start SIM WARMUP, then the existing5s/10s simulation and Basket: pending.

**Check before continuing:** ask whether the held index was rejected, release changed the prompt without advancing, and only re-actuation started warm-up. Wait for the physical result before the startup-held-flavor test or further work. No code, flash, monitor opening or wiring changes. If the deadline expires, obtain actual displayed stages/operation order; do not infer a defective input. RESET remains a bench reset, not a hardware safety-stop function.

**Step23 user result:** User reports “working as intended” after Step23: index1 held before flavor1 selection produces SIM RELEASE IDX and does not start warm-up; release changes to SIM PRESS INDEX without advancing; a fresh index1 actuation advances the simulation. Record selected-index release/re-actuation qualification as PASS by user report. No independently measured timing or manual serial trace supplied; no mechanical homing or motor protection qualification inferred.

## Current checkpoint: Step24 complete — USB-only logic milestone passed

User reports “working as intended” after Step24: flavor3 held through onboard RESET stays idle after startup, releasing it also leaves idle, and only a fresh press selects Flavor3. The matching index3 permits the simulated sequence. Record startup-held flavor suppression as PASS by user report. No manual-event serial capture or precise timing readings supplied.

All currently planned USB-only input/display/control-logic checks now pass. Current firmware and wires remain unchanged; no new build, flash, monitor session or device action. See [USB_LOGIC_CHECKPOINT.md](USB_LOGIC_CHECKPOINT.md) for the concise resume point and coverage limits.

**Full Phase2 prototype remains incomplete.** Next priority is the already planned regulated enclosed12V5A60W adapter; four additional basket-input switches remain to buy. Other power wiring/protection/mounting details are not automatically qualified. When the adapter arrives, request its label/plug photo before issuing a measured-output/polarity checkpoint or any motor wiring. Do not repeat passed USB checks absent new evidence; no Phase3 transition or powered motor/heater action.

## Subsequent checkpoints — not instructions to perform yet

| Stage | Evidence needed before issuing its physical instructions |
|---|---|
| Bare Mega USB checkpoint | Basic power and enumeration passed; retain no-external-wiring arrangement |
| Onboard-LED/serial diagnostic | Step 4 complete: setup/build/upload/serial and user LED observation passed |
| LCD check | LCD text/contrast passed; keep same wires/address0x27 |
| Button input firmware | Step11 uploaded; all buttons working per user after pin correction; separate hold details not itemised |
| Index input firmware | D26 index1 diagnostic uploaded and physical test passed by user; two other inputs follow shared-ground rail verification |
| MOSFET/motor channel test | Actual soldered board/pin labels, safe OFF/reset handling, validated DC supply/protection, measured polarity, secured unloaded motor and disconnect arrangement |
| Three-channel dispenser test | Individual channel passes, mounts/couplings/cams and packet/coil fit, then jam/index fault handling |
| Basket/fryer integration | Separate mechanical/power/stop/protection requirements met; qualified mains review and later explicit test steps |

User approved Step 4 execution. Project-local CLI 1.5.1 / AVR Boards 1.8.8 setup, diagnostic compilation/upload and serial heartbeat/ACK have now passed; exact commands and evidence are in ARDUINO_SETUP.md and .build/logs/. hd447801.3.2 was subsequently installed after approval for Step9; no new USB driver installed. The user has now confirmed the expected LED pattern. LCD four-wire connection and first USB-only power observation now issued; no actuator operation.
